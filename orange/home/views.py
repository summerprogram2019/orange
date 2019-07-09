from django.shortcuts import render
from accounts.models import AteFood
from datetime import datetime

# Create your views here.

def index(request):
    current_user = request.user
    today = datetime.now().date()

    if current_user.is_authenticated:

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
                total_vitamin_today += i.food.nutrients.__getattribute__(vitamin)

            today_vitamins.append(total_vitamin_today)
            percent.append(int(100*total_vitamin_today/daily_intake))

        args = {
            'intakes' : zip(daily_intake_names, daily_intake_values, today_vitamins, percent)
        }

    else:
        args = {}

    return render(request, 'home/index.html', args)