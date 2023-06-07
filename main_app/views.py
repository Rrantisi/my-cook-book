from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.http import JsonResponse
from .models import Recipe
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

def get_recipe_data(request):
    query = request.GET.get('query')
    url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={query}&limit=5'
    response = requests.get(url)
    data = response.json()
    result = data.get('meals')
    print(result)
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
    return JsonResponse({'result': result})

def recipes_index(request):
    recipes = Recipe.objects.filter(user = request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'region']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'region']

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes/'