from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Portfolio
from .forms import CustomAuthForm
from django.views.generic import ListView
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required#
from django.forms.utils import ErrorList


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class view_home(ListView):
    model = Portfolio
    template_name = 'home.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navbar'] = 'home'
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['MEDIA_ROOT'] = settings.MEDIA_ROOT
        return context
    

def view_signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully Created for {username} Login In Now!!!')
            return redirect('signin')
        else:
            # If the form is not valid, add the error messages to the template context
            context = {'form': form}
            if 'username' in form.errors:
                context['username_errors'] = form.errors['username']
            if 'email' in form.errors:
                context['email_errors'] = form.errors['email']
            if 'password1' in form.errors:
                context['password1_errors'] = form.errors['password1']
            if 'password2' in form.errors:
                context['password2_errors'] = form.errors['password2']
            return render(request, 'signup.html', context)
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

def view_signin(request): 
    if request.method == 'POST':
        form = CustomAuthForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form, 'navbar': 'signin'})

def view_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create.html', {'form': form, 'navbar':'create'})

