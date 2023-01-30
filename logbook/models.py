from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", null=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    registration_number = models.CharField(max_length=25, verbose_name="Registration Number", null=True)

    def __str__(self):
        return self.user.username
    

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
    

class DailyReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    activity = models.TextField()
    working_hours = models.IntegerField(verbose_name='Workin Hours')

    def __str__(self):
        return self.activity


class WeeklyReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    report = models.TextField()


    def __str__(self):
        return self.date
