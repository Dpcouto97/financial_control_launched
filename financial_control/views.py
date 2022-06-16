from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import User

# Create your views here.
def homepage_view(request):
    return render(request, "home.html")


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        username = form.data.get("username")
        password = form.data.get("password")

        user = authenticate(request, username=username, password=password)
        #If the user is authenticated and valid
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage-view'))
        else:
            messages.info(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'accounts/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage-view'))