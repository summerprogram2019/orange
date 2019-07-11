from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Form used for registration
class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'weight',
            'height',
            'sex',
            'profile',
            'picture',
        )

# Form to edit details
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = (
            'weight',
            'height',
            'profile',
            'picture',
        )
        exclude = ('password1', 'password2',)
