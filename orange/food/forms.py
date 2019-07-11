from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from food.models import Nutrition

# Form used for registration
class NutritionForm(forms.ModelForm):

    class Meta:
        model = Nutrition
        exclude=()