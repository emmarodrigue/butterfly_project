from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import EditAccountForm
from django.shortcuts import render, redirect
from django.views import generic
from .models import *


# main pages
def landing(request):
    return render(request, 'landing.html')


def resources(request):
    return render(request, 'resources.html')


def homelessness_in_america(request):
    return render(request, 'homelessness_in_america.html')


def how_to_help(request):
    return render(request, 'how_to_help.html')


# registration/login
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Sign up successful!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in. Try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})


@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


# account
@login_required(login_url='/login')
def account(request):
    return render(request, 'account.html')


class UserChangeView(generic.UpdateView):
    form_class = EditAccountForm
    template_name = 'edit_account.html'
    success_url = 'account'

    def get_object(self):
        return self.request.user


@login_required(login_url='/login')
def edit_account(request):
    return render(request, 'edit_account.html')


# saved resources
@login_required(login_url='/login')
def saved_resources(request):
    return render(request, 'saved_resources.html')


# contact/help
def contact(request):
    return render(request, 'contact.html')


def report(request):
    return render(request, 'report.html')

def healthcare(request):
    return render(request, 'healthcare.html')

def food(request):
    return render(request, 'food.html')

def specific_populations(request):
    return render(request, 'specific_populations.html')

def answer(request):
    return render(request, 'answer.html')