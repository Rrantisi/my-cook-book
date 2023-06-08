from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('find/', views.find, name='find'),
    path('recipes/', views.recipes_index, name='index'),
    path('recipes/<int:recipe_id>', views.recipes_detail, name='detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'), 
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'), 
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'), 
    path('recipes/<int:recipe_id>/add_instruction/', views.add_instruction, name='add_instruction'), 
    path('recipes/<int:recipe_id>/add_ingredient/', views.add_ingredient, name='add_ingredient'), 
    path('recipes/find_recipes/', views.find_matching_recipes, name='find_matching_recipes'),
    path('tags/', views.TagList.as_view(), name='tags_index'), 
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'), 
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag_details'), 
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag_update'), 
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'), 
    path('tags/<int:recipe_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
    path('tags/<int:recipe_id>/unassoc_tag/<int:tag_id>/', views.unassoc_tag, name='unassoc_tag'),
    path('accounts/signup/', views.signup, name='signup'),
    path('api/recipes/', views.get_recipe_data, name='get_recipe_data'),
    path('api/recipes/<str:recipe_name>/', views.get_recipe_details, name='get_recipe_details'),
]