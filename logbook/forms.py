from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class StudentSignUpForm(UserCreationForm):
    registration_number = forms.CharField(max_length=25)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('registration_number',)



class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = ['activity', 'working_hours']


class WeeklyReportForm(forms.ModelForm):
    class Meta:
        model = WeeklyReport
        fields = ['heading', 'text']


class ArrivalNoteForm(forms.ModelForm):
    class Meta:
        model = ArrivalNote
        fields = ['location', 'organization_name']


class RecommandationForm(forms.ModelForm):
    class Meta:
        model = Recommandation
        fields = ['text',]