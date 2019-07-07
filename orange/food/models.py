from django.db import models

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
    nutrients = models.ForeignKey(Nutrition, on_delete=models.CASCADE, verbose_name="Nutrition")

    def __str__(self):
        return self.name


class Profile(models.Model):
    # name to help user choose profile
    name = models.CharField(max_length=40)

    weight = models.DecimalField(max_digits=5, decimal_places=2) # kg
    height = models.DecimalField(max_digits=5, decimal_places=2) # cm

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    daily_intake = models.ForeignKey(Nutrition, on_delete=models.CASCADE, verbose_name="Nutrition")

    def __str__(self):
        return self.name
