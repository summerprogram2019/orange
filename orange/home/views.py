from django.shortcuts import render
from accounts.models import AteFood
from datetime import datetime
from food.api import lookup, reverse_lookup

# Create your views here.

def index(request):
    current_user = request.user
    today = datetime.now().date()

    if current_user.is_authenticated and current_user.profile is not None:

        daily_intake_names = [x.name for x in current_user.profile.daily_intake._meta.fields
                if x.name != 'id']


        daily_intake_values = [current_user.profile.daily_intake.__getattribute__(x)
                for x in daily_intake_names if x != 'id']

        today_food = AteFood.objects.filter(person=current_user, timestamp__gte=today)

        today_vitamins = []

        percent = []

        for vitamin, daily_intake in zip(daily_intake_names, daily_intake_values):

            total_vitamin_today = 0

            # calculate amount eaten today
            for i in today_food:
                if i.food.nutrients.__getattribute__(vitamin) is not None:
                    total_vitamin_today += i.food.nutrients.__getattribute__(vitamin)

            today_vitamins.append(total_vitamin_today)
            percent.append(int(100*total_vitamin_today/daily_intake))

        # convert units to strings
        units = ['{:~}'.format(lookup[reverse_lookup[x]][1]) for x in daily_intake_names]

        daily_intake_names = [' '.join([y.capitalize() for y in x.replace("_", " ").split(" ")])
                for x in daily_intake_names]

        daily_intake_values = [str(round(x, 0)) for x in daily_intake_values]
        today_vitamins = [str(round(x, 0)) for x in today_vitamins]

        args = {
            'intakes' : sorted(zip(daily_intake_names,
                    daily_intake_values, today_vitamins, percent, units))
        }

    else:
        args = {}

    return render(request, 'home/index.html', args)