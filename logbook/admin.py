from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_student', 'is_supervisor']

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(DailyReport)
admin.site.register(Supervisor)
