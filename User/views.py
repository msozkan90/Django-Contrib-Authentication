from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        password1= form.data.get('password1')
        password2= form.data.get('password2')
        username= form.data.get('username')
        email = form.data.get('email')
        email_check=User.objects.filter(email=email)
        users=User.objects.filter(username=username)
        try:
            if form.is_valid:
                user = form.save(commit=False)
                user.save()
                messages.success(request,"You registered successfully. Please log in.")
                return redirect("login")
        except(ValueError):
            if(password1 != password2):
                messages.warning(request,"Passwords did not match")
                return redirect("register")
            if(users):
                messages.warning(request,"This user name is already taken")
                return redirect("register")
            if(email_check):
                messages.warning(request,"This email is already taken")
                return redirect("register")
            
    return render(request,"registration/register.html",{"form":form})


