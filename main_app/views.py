from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.http import JsonResponse
from .models import Recipe, Instruction
import requests

def home(request):
  return render(request, 'home.html')

def signup(request):
    error_message = ''
    # POST request
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/') #UPDATE IT
        else:
            error_message = 'Invalid signup - try again'
    # GET request
    form = UserCreationForm() 
    return render(request, 'registration/signup.html', 
    {'form': form,
    'error': error_message}
    )

@login_required
def get_recipe_data(request):
    query = request.GET.get('query')
    url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={query}'
    response = requests.get(url)
    data = response.json()
    result = data.get('meals')
    def is_attribute_present(attribute_value):
        # Query the model to check if any objects have the same attribute value
        matching_objects = Recipe.objects.filter(name=attribute_value)
        # If there are any matching objects, attribute_value is already present
        if matching_objects.exists():
            return True
        else:
            return False

    for r in result:
        if (is_attribute_present(r.get('strMeal'))) != True :
            new_recipe = Recipe(
                name = r.get('strMeal'),
                region = r.get('strArea'),
                user = request.user
            )
            new_recipe.save()
            all_steps = r.get('strInstructions').split('\r\n')
            for s in all_steps:
                Instruction.objects.create(
                    recipe=new_recipe,
                    step=s
                )
    return JsonResponse({'result': result})

def get_recipe_details(request, recipe_name):
    recipe = Recipe.objects.get(name=recipe_name)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

@login_required
def recipes_index(request):
    recipes = Recipe.objects.filter(user = request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'region']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'region']

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'