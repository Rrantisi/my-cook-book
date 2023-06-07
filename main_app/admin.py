from django.contrib import admin
from .models import Recipe, Instruction, Ingredient

admin.site.register([Recipe, Instruction, Ingredient])
