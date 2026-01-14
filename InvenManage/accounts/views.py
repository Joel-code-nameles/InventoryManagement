from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Registration
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Register(request):
    if request.method == "POST":
        userEmail = request.POST['email']
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
            userEmail = userEmail,
            username = username,
            password = hashed_password,
            
        )
        userAccount.save()
        messages.success(request, "Account created")
        return redirect('login')

    return render(request, "pages/register.html")


def Login(request):
    if request.method == 'POST':
        userEmail = request.POST.get("userEmail")
        password = request.POST.get("password")

        try:
            user = Registration.objects.get(userEmail__iexact = userEmail)

            if check_password(password, user.password):
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                messages.success(request, f"Welcome {user.username}")
                return redirect('dashboard')

        except Registration.DoesNotExist:
            pass
        messages.error(request, "Wrong Email or Password")
        return redirect('login')


    return render(request, "pages/login.html")


def dashboard(request):
    return render(request, 'pages/dashboard.html')