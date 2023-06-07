from django import forms
from django.forms import ModelForm
from .models import Instruction, Ingredient

class InstructionForm(ModelForm): 
    step = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Instruction
        fields = ['step']

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'amount']

    
