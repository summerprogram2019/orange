from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('add_food/', views.add_food, name='add_food'),
    path('view_all_food/', views.view_all_food, name='view_all_food'),
    path('view_food/<int:id>/', views.view_food, name='view_food'),
    path('add_food/<int:id>/', views.add_food, name='add_food'),
    path('search_food/<foodname>/', views.search_food, name='search_food'),
    path('scan_food', views.scan_food, name='scan_food'),
    path('food_diary', views.food_diary, name='food_diary'),
    path('professionals', views.professionals, name='professionals'),
]
