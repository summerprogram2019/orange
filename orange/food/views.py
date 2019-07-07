from django.shortcuts import render

# Create your views here.
def add_food(request):
    return render(request, 'food/add_food.html')
