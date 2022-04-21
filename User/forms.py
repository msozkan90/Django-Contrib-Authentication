from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Checking the email address is taken or not
def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise forms.ValidationError((f"{value} is taken."),params = {'value':value})


# Created Registration Form for registration function
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(validators = [validate_email])
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
