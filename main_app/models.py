from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name

