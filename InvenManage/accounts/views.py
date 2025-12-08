from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Registration
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        if password != conf_password:
            messages.error(request,"Passwords do not match.")
            return redirect('register')

        if Registration.objects.filter(username = username).exists():
            messages.error(request, "Username is already in existence")
            return redirect('register')

