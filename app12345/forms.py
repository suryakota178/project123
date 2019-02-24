from django import forms
from app12345.models import UserProfile
from django.contrib.auth.models import User
from app12345.models import Actor

class Form1(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class Form2(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=('website',)


class ActorForm(forms.ModelForm):
    class Meta():
        model=Actor
        fields=('__all__')


