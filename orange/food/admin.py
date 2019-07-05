from django.contrib import admin
from food.models import Food, Nutrition, AteFood, Profile

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    model = Food

class NutritionAdmin(admin.ModelAdmin):
    model = Nutrition

class AteFoodAdmin(admin.ModelAdmin):
    model = AteFood

class ProfileAdmin(admin.ModelAdmin):
    model = Profile

admin.site.register(Food, FoodAdmin)
admin.site.register(Nutrition, NutritionAdmin)
admin.site.register(Profile, ProfileAdmin)
