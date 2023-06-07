from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self): 
        return reverse('detail', kwargs={'recipe_id': self.id})
    
    class Meta:
        ordering = ['name']


class Instruction(models.Model):
    step = models.CharField(max_length=800)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step

