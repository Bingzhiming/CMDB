from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.shortcuts import redirect, reverse

REDIRECT_URL='/user/login'

@login_required(login_url=REDIRECT_URL)
def logout_user(request) :
    logout(request)
    return redirect(reverse('user_login_user'))

def login_user(request) :
    if request.method == 'POST' :
        form = LoginForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=name, password=password)
            if user is None :
                return render(request, 'user/login.html')
            login(request, user)
            next = request.GET.get('next')
            if next is None :
                return redirect(reverse('pc_pcs'))
            else :
                return redirect(next)
    else:
        return render(request, 'user/login.html')

# Create your views here.
def register(request) :
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password_again = form.cleaned_data.get('password_again')
            if password != password_again :
                return render(request, 'user/register.html')
            user = User(username=name, email=email)
            user.set_password(password)
            user.is_active = True
            try:
                user.save()
            except :
                render(request, 'user/register.html')
            return render(request, 'user/register.html')
    else:
        return render(request, 'user/register.html')
