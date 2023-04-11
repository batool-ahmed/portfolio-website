from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Portfolio

class PostForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'createField'}),
            'content': forms.Textarea(attrs={'class': 'createField', 'rows': 5}),
            'image': forms.FileInput(),

        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'signinField', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'signinField', 'placeholder': 'Password'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'signinField', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'signinField', 'placeholder': 'Password'})
