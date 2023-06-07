from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.http import JsonResponse
import requests
from .models import Recipe, Instruction, Ingredient
from .forms import InstructionForm, IngredientForm

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
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            query = request.GET.get('s')
            url = f'https://www.themealdb.com/api/json/v1/1/search.php?s={query}'
            response = requests.get(url)
            data = response.json()
            result = data.get('meals')
            #--- Check to see if recipe is already added to db by comparing recipe name ---#
            def is_present(recipe_name):
                matching_objects = Recipe.objects.filter(name=recipe_name)
                if matching_objects.exists():
                    return True
                else:
                    return False
            for r in result:
                #--- if recipe isn't present yet, add it to db ---#
                if not (is_present(r.get('strMeal'))) :
                    new_recipe = Recipe(
                        name = r.get('strMeal'),
                        region = r.get('strArea'),
                        user = request.user
                    )
                    new_recipe.save()
                #--- fetch recipe instructions and use split method to turn it into an array of steps ---#
                    all_steps = r.get('strInstructions').split('\r\n')
                #--- if after splitting there are empty elements, remove them ---#
                    for index, element in enumerate(all_steps):
                        if not element:
                            all_steps.pop(index)
                #--- use the final version of all_steps to create a new object instance of instruction and assign it to same recipe ---#
                    for s in all_steps:
                        Instruction.objects.create(
                            recipe=new_recipe,
                            step=s
                        )
                #--- iterate through the ingredient and measure and add them all to a list of dictionaries ---#
                    ingredients = []
                    for i in range(1, 21):
                        ingredient = r.get(f'strIngredient{i}')
                        measure = r.get(f'strMeasure{i}')
                        if ingredient:
                            ingredients.append({'ingredient': ingredient, 'measure': measure})
                    for dict in ingredients:
                        Ingredient.objects.create(
                            recipe = new_recipe,
                            name = dict['ingredient'],
                            amount = dict['measure']
                        )
            return JsonResponse({'result': result})

@login_required
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
    instruction_form = InstructionForm()
    ingredient_form = IngredientForm()
    return render(request, 'recipes/detail.html', 
    {'recipe': recipe, 'instruction_form': instruction_form, 'ingredient_form': ingredient_form})

@login_required
def add_instruction(request, recipe_id):
    # creates a form instance from InstructionForm (an object from the form and its able to grab that through the request.POST)
    form = InstructionForm(request.POST) 
    if form.is_valid():
        new_step = form.save(commit=False)
        new_step.recipe_id = recipe_id
        new_step.save()
    return redirect('detail', recipe_id=recipe_id)

@login_required
def add_ingredient(request, recipe_id):
    form = IngredientForm(request.POST) 
    if form.is_valid():
        new_ingredient = form.save(commit=False)
        new_ingredient.recipe_id = recipe_id
        new_ingredient.save()
    return redirect('detail', recipe_id=recipe_id)

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

