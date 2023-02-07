from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", null=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    registration_number = models.CharField(max_length=25, verbose_name="Registration Number", null=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def assign_to_supervisor(sender, instance, **kwargs):
    if instance.is_supervisor:
        supervisor, created = Supervisor.objects.get_or_create(user=instance)
        if created:
            supervisor.save()
post_save.connect(assign_to_supervisor, sender=User)
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
    heading = models.CharField(max_length=250, null=True)
    text = models.TextField()
    # imagge = models.ImageField(upload_to='students/report/images', null=True)


    def __str__(self):
        return self.heading


class Recommandation(models.Model):
    date = models.DateField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.student.user.username

class ArrivalNote(models.Model):
    date = models.DateField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

    def __str__(self):
        return self.student.user.username
