# Generated by Django 4.2.2 on 2023-06-09 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_tag_recipe_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.recipe')),
            ],
        ),
    ]
