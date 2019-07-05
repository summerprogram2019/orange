from django.db import models
from accounts.models import User

# Create your models here.

#TODO unit conversions

class Nutrition(models.Model):
    calcium = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    calories = models.DecimalField(max_digits=9, decimal_places=3, null=True) # Cal
    fat = models.DecimalField(max_digits=9, decimal_places=3, null=True) # g
    sat_fat = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    sodium = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    carbs = models.DecimalField(max_digits=9, decimal_places=3, null=True) # g
    fibre = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    protein = models.DecimalField(max_digits=9, decimal_places=3, null=True) # g
    vitamin_a = models.DecimalField(max_digits=9, decimal_places=3, null=True) # IU
    vitamin_b12 = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    vitamin_b6 = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    vitamin_c = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    vitamin_d = models.DecimalField(max_digits=9, decimal_places=3, null=True) # IU
    vitamin_e = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    niacin = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    thiamin = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    phosphorus = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    zinc = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    magnesium = models.DecimalField(max_digits=9, decimal_places=3, null=True) # mg
    folate = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg
    riboflavin = models.DecimalField(max_digits=9, decimal_places=3, null=True) # µg


class Food(models.Model):
    name = models.CharField(max_length=40)
    nutrients = models.ForeignKey("Nutrition", on_delete=models.CASCADE, verbose_name="Nutrition")

class AteFood(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person")
    food = models.ForeignKey("Food", on_delete=models.CASCADE, related_name="food")
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)

class Profile(models.Model):
    weight = models.DecimalField(max_digits=5, decimal_places=2) # kg
    height = models.DecimalField(max_digits=5, decimal_places=2) # cm
    daily_intake = models.ForeignKey("Nutrition", on_delete=models.CASCADE, verbose_name="Nutrition")
    