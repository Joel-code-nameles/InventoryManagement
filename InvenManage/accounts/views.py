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

        hashed_password = make_password(password)

        userAccount = Registration.objects.create(
            email = email,
            username = username,
            password = password,

        )
        userAccount.save()
        messages.success(request, "Account already created")
        return redirect('login')

    return render(request, "pages/register.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            userAccount = Registration.objects.get(email = email)

            if check_password(password, userAccount.password):
                messages.success(request, f"Let Get Managing {userAccount.username}")
                return render(request, "pages/login.html")

            else:
                messages.error(request, "Wrong Password")
                return redirect('login')

        except Registration.DoesNotExist():
            messages.error(request, "Wrong Email or Password")
            return redirect('login')

    return render(request, "pages/Dashboard.html")