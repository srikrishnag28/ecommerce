from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from accounts.models import Account
from django.contrib.auth import authenticate, login, logout
from cart.models import Cart, CartItems

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number
            )
            user.set_password(password)

            messages.success(request, 'Account created successfully!!')
            return redirect('login')
        else:
            if 'email' in form.errors:
                messages.error(request, 'Account with email already exists!!')
            elif 'password' in form.errors:
                messages.error(request, 'Password did not match!!')
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    next_url = request.POST.get('next')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        print(email, password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('cart')
        else:
            if not Account.objects.filter(email=email).exists():
                messages.error(request, 'Invalid email. User does not exist!')
            else:
                messages.error(request, 'Invalid password!')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully!!')
    return redirect('login')
