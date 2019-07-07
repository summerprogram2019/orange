from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('add_food/', views.add_food, name='add_food'),
]
