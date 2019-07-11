from django.shortcuts import render, redirect
from food.models import Food, Nutrition
from accounts.models import AteFood
from datetime import datetime
from food.api import get_nutrients, lookup, reverse_lookup
from decimal import *

# Create your views here.
def scan_food(request):
    return render(request, 'food/scan_food.html')


def view_all_food(request):

    args = {
        'foods' : Food.objects.all()
    }

    return render(request, 'food/view_all_food.html', args)


def view_food(request, id):
    food = Food.objects.get(pk=id)

    # get name, value and units for this food
    daily_intake_names = [x.name for x in food.nutrients._meta.fields
            if x.name != 'id']

    daily_intake_values = [food.nutrients.__getattribute__(x)
            for x in daily_intake_names if x != 'id']

    units = ['{:~}'.format(lookup[reverse_lookup[x]][1]) for x in daily_intake_names]

    daily_intake_names = [' '.join([y.capitalize() for y in x.replace("_", " ").split(" ")])
            for x in daily_intake_names]

    args = {
        'food' : food,
        'data' : zip(daily_intake_names, daily_intake_values, units)
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

def food_error(request, foodname):

    args = {
        'foodname' : foodname
    }

    return render(request, 'food/food_error.html', args)

def search_food(request, foodname):

    food_object = None

    # first check if this food already exists
    for x in Food.objects.all():
        if x.name == foodname:
            food_object = x
            break

    # food already exists
    if food_object is not None:
        return redirect(f'/food/view_food/{food_object.id}')

    # food doesn't exist
    # attempt to get from wolfram alpha api
    nutrients = get_nutrients(foodname)
    
    if nutrients is None:
        return redirect(f'/food/food_error/{foodname}')

    else:
        # convert the resulting units according to the lookup table
        converted = {}

        # convert to units
        for name, quantity in nutrients.items():
            # convert unit and save
            converted[name] = quantity.to(lookup[reverse_lookup[name]][1]).m

        # create new nutrient
        nutrient = Nutrition(**converted)
        nutrient.save()

        # create new food in database
        food = Food(nutrients=nutrient, name=foodname)
        food.save()

        # go to new page
        return redirect(f'/food/view_food/{food.id}')
