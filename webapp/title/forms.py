from django import forms
from title.models import UserProfileInfo
from title.models import Monitoring
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')

    

class MonitoringForm(forms.ModelForm):
    class Meta():
        model = Monitoring
        fields = ('name','url','body')