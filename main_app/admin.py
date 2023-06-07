from django.contrib import admin
from .models import Recipe, Instruction

admin.site.register([Recipe, Instruction])
