from django.contrib import admin
from .models import Recipe, Instruction, Ingredient, Tag, Photo

admin.site.register([Recipe, Instruction, Ingredient, Tag, Photo])
