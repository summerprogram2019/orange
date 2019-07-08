from django.contrib import admin
from food.models import Food, Nutrition, Profile
from accounts.models import AteFood

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
admin.site.register(AteFood, AteFoodAdmin)
