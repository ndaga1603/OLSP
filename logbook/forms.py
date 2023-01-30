from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django.shortcuts import redirect



class StudentSignUpForm(UserCreationForm):
    registration_number = forms.CharField(max_length=25)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('registration_number',)



class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = ['activity', 'working_hours']
