from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'is_student', 'is_supervisor', 'phone_number')

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    list_display = ['username', 'is_student', 'is_supervisor']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.cleaned_data['password'])
        obj.save()




class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'registration_number']

class StudentWeeklyReport(admin.ModelAdmin):
    list_display = ['student', 'heading', 'date']


class StudentDailyReport(admin.ModelAdmin):
    list_display = ['student', 'date', 'working_hours']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(DailyReport, StudentDailyReport)
admin.site.register(Supervisor)
admin.site.register(WeeklyReport, StudentWeeklyReport)
admin.site.register(ArrivalNote)
admin.site.register(Recommandation)
