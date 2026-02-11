from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product

# =========================
# REGISTER VIEW
# =========================
def Register(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        conf_password = request.POST.get('conf_password', '').strip()

        # Validate required fields
        if not username or not email or not password or not conf_password:
            messages.error(request, "All fields are required")
            return redirect('register')

        # Check password match
        if password != conf_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # Check if email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # Create the user (use create_user to hash the password)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, "pages/register.html")


# =========================
# LOGIN VIEW - FIXED
# =========================
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Validate required fields
        if not username or not password:
            messages.error(request, "Both fields are required")
            return redirect('login')

        # Authenticate the user using the built-in User model
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "pages/login.html")


# =========================
# LOGOUT VIEW
# =========================
@login_required
def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


# =========================
# DASHBOARD VIEW
# =========================
@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')


# =========================
# INVENTORY PAGE
# =========================
@login_required
def inventory(request):
    products = Product.objects.all()
    return render(request, 'pages/inventory.html', {
        'products': products
    })


# =========================
# ADD PRODUCT VIEW
# =========================
@login_required
def add_product(request):
    if request.method == 'POST':
        SKU = request.POST.get('SKU', '').strip()
        product_name = request.POST.get('product_name', '').strip()
        category = request.POST.get('category', '').strip()
        description = request.POST.get('description', '').strip()
        price = request.POST.get('price', '').strip()
        sales_price = request.POST.get('sales_price', '').strip()
        initial_quantity = request.POST.get('initial_quantity', '').strip()
        low_stock_alert = request.POST.get('low_stock_alert', '').strip()

        # Validate required fields
        if not SKU or not product_name or not price or not initial_quantity:
            messages.error(request, "All required fields must be filled")
            return redirect('add_product')

        # Create the product
        Product.objects.create(
            SKU=SKU,
            product_name=product_name,
            category=category,
            description=description,
            price=price,
            sales_price=sales_price,
            initial_quantity=initial_quantity,
            low_stock_alert=low_stock_alert,
            user=request.user
        )

        messages.success(request, "Product added successfully")
        return redirect('inventory')

    return render(request, 'pages/add_product.html')


# =========================
# STOCK PAGE
# =========================
@login_required
def stock(request):
    products = Product.objects.all()
    return render(request, 'pages/stock.html', {
        'products': products
    })

@login_required
def invoices(request):
    products = Product.objects.all()
    return render(request, 'pages/invoice.html')

@login_required
def create_invoices(request):
    products = Product.objects.all()
    return render(request, 'pages/create_invoice.html')


# =========================
# PRODUCT LIST VIEW
# =========================
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'pages/product_list.html', {
        'products': products
    })