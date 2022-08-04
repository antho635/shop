from django.contrib.auth import login, get_user_model, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import Shopper

User = get_user_model()


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,
                                        password=password
                                        )
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')
