from django import forms
from django.forms import ModelForm
from .models import Instruction

class InstructionForm(ModelForm): 
    step = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Instruction
        fields = ['step']

    
