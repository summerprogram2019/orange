from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from food.models import Profile, Food

# Create your models here.
class Person(AbstractUser):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="profile", null=True)
    picture = models.ImageField(upload_to="uploaded/", null=True, blank=True)

# here to resolve circular dependency
class AteFood(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="food")
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
