from django.shortcuts import render, redirect
from food.models import Food
from accounts.models import AteFood
from datetime import datetime

# Create your views here.
def scan_food(request):
    return render(request, 'food/scan_food.html')


def view_all_food(request):

    args = {
        'foods' : Food.objects.all()
    }

    return render(request, 'food/view_all_food.html', args)


def view_food(request, id):

    args = {
        'food' : Food.objects.get(pk=id)
    }

    return render(request, 'food/view_food.html', args)


def add_food(request, id):

    # add to food diary
    atefood = AteFood(person=request.user, food=Food.objects.get(pk=id))
    atefood.save()

    return redirect('/')

def food_diary(request):
    current_user = request.user
    today = datetime.now().date()

    args = {
        'today_atefood' : AteFood.objects.filter(person=current_user, timestamp__gte=today),
        'yesterday_atefood' : AteFood.objects.filter(person=current_user, timestamp__lt=today)
    }

    return render(request, 'food/food_diary.html', args)

def professionals(request):

    return render(request, 'food/professionals.html')
