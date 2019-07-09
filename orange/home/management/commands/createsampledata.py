from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from django.db.utils import IntegrityError

from food.models import Nutrition, Profile

# creates some sample data to save time
class Command(BaseCommand):
    # Show this when the user types help
    help = "Creates some sample data"

    def handle(self, *args, **options):
        
        average_nutrition = Nutrition(
            calories=2000,
            calcium=1000,
            fat=70,
            protein=50,
            sat_fat=24,
            sodium=2300,
            carbs=310,
            fibre=30,
            vitamin_a=600,
            vitamin_b12=6,
            vitamin_b6=2000,
            vitamin_c=75,
            vitamin_d=5000,
            vitamin_e=10,
            niacin=18,
            thiamin=1400,
            phosphorus=1000,
            zinc=15,
            magnesium=350,
            folate=400,
            riboflavin=1600,
        )
        average_nutrition.save()

        average_profile = Profile(name="Average Nutrition", daily_intake=average_nutrition)
        average_profile.save()

        cataracts_nutrition = Nutrition(
            calories=2000,
            calcium=1000,
            fat=70,
            protein=50,
            sat_fat=24,
            sodium=2300,
            carbs=310,
            fibre=30,
            vitamin_a=600,
            vitamin_b12=6,
            vitamin_b6=2000,
            vitamin_c=75,
            vitamin_d=5000,
            vitamin_e=10,
            niacin=18,
            thiamin=1400,
            phosphorus=1000,
            zinc=15,
            magnesium=350,
            folate=400,
            riboflavin=3000,
        )
        cataracts_nutrition.save()

        cataracts_profile = Profile(name="Increased riboflavin for cataract prevention", 
                daily_intake=cataracts_nutrition)
        cataracts_profile.save()
        