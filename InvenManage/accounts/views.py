from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Registration
from .models import Product
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def Register(request):
    if request.method == "POST":
        userEmail = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if username == '':
            messages.error(request, 'All fields required')
            return redirect('register')

        if userEmail == '':
           messages.error(request, 'All fields required')
           return redirect('register')

        if password == '':
            messages.error(request, 'All fiels required')
            return redirect('register')

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
        messages.success(request, "Account successfully created")
        return redirect('dashboard')

    return render(request, "pages/register.html")


def Login(request):
    if request.method == 'POST':
        userEmail = request.POST.get('userEmail')
        password = request.POST.get('password')

        try:
            user = Registration.objects.get(userEmail__iexact=userEmail)

            if userEmail == '':
                messages.error(request, 'All fields required')
                return redirect('login')
            
            if password == '':
                messages.error(request, 'All fields required')
                return redirect('login')

            if check_password(password, user.password):
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                messages.success(request, f"Welcome {user.username}")
                return redirect('dashboard')

        except Registration.DoesNotExist:
            pass

        messages.error(request, "Wrong Email or Password")
        return redirect('login')

    return render(request, "pages/login.html")

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def inventory(request):
    return render(request, 'pages/inventory.html')

def add_product(request):
    if request.method == 'POST':
        SKU = request.POST.get('SKU')
        product_name = request.POST.get('product_name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        sales_price = request.POST.get('sales_price')
        initial_quantity = request.POST.get('initial_quantity')
        low_stock_alert = request.POST.get('low_stock_alert')

        if SKU == '':
            messages.error(request, 'All fields required')

        product_acc = Product.objects.create(
            SKU = SKU,
            product_name = product_name,
            category = category,
            description = description,
            price = price,
            sales_price = sales_price,
            initial_quantity = initial_quantity,
            low_stock_alert = low_stock_alert,
        )
        product_acc.save()
        messages.success(request, 'Products added successfully')
        return redirect('add_products')

    return render(request, 'pages/add_product.html')

def stock(request):
    return render(request, 'pages/stock.html')