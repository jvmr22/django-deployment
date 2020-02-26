from basic_app.models import UserProfile
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)
    class Meta():
        # model = UserProfile #copy all columns of model
        model=User
        # exclude = ('user',)
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile #copy all columns of model
        fields = ('portfolio','picture')
