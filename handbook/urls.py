from django.urls import path
from handbook import views

# moves:move
app_name = 'moves'

urlpatterns = [
    path('', views.home, name='home'),
    path('moves/search/', views.search_def, name='search'),
    path('moves/dificuldades/<int:difficulty_id>/', views.difficulty_def, name="difficulty"),  # noqa:E501
    path('moves/categorias/<int:category_id>/', views.category_def, name="category"),  # noqa:E501
    path('moves/<int:movement_id>/', views.move, name="move"),
]
