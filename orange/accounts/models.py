from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from food.models import Profile, Food

# Create your models here.
class Person(AbstractUser):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="profile", null=True)
    picture = models.ImageField(upload_to="uploaded/profile_pictures/", null=True, blank=True)

    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True) # kg
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True) # cm

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='M')

# here to resolve circular dependency
class AteFood(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="food")
    timestamp = models.DateTimeField(auto_now_add=True)
