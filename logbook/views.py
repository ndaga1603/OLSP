from django.contrib.auth import login
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

class StudentRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Student access only"

    def test_func(self):
        return self.request.user.is_student


class SupervisorRequiredMixin(UserPassesTestMixin):
    raise_exception = True
    permission_denied_message = "Supervisor access only"

    def test_func(self):
        return self.request.user.is_supervisor
    

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_student = True
        user = form.save()
        # login(self.request, user)
        student = Student.objects.create(
            user=user, registration_number=form.cleaned_data.get('registration_number'))
        return redirect('login')


class Homepage(TemplateView):
    template_name = "index.html"


class StudentView(LoginRequiredMixin, StudentRequiredMixin, TemplateView):
    template_name = 'student.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.request.user.id
        number_of_daily_reports = DailyReport.objects.filter(student=student).count()
        number_of_weekly_reports = WeeklyReport.objects.filter(student=student).count()
        total = number_of_daily_reports + number_of_weekly_reports
        context["total"] = total
        return context
    

class SupervisorView(LoginRequiredMixin, SupervisorRequiredMixin, TemplateView):
    template_name = 'supervisor.html'
    login_url = '/login/'



class WeeklyReportView(TemplateView):
    template_name = 'weekly-report.html'


class DailyReportView(ListView):
    template_name = 'daily-report.html'
    model = DailyReport


class CreateDailyReport(StudentRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "daily.html"
    form_class = DailyReportForm
    login_url = '/login/'
    success_url = reverse_lazy('student')

    def form_valid(self, form):
        user = self.request.user
        if user.is_student:
            form.instance.student = user.student
        return super().form_valid(form)


class CreateWeeklyReport(TemplateView):
    template_name = "weekly.html"


class ArivalNoteView(TemplateView):
    template_name = "arival-note.html"


class CreateArivalNote(TemplateView):
    template_name = "arivalnote.html"


class CreateRecommendation(TemplateView):
    template_name = "recommendation.html"


class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.is_student:
            self.next_page = 'student'
        elif user.is_supervisor:
            self.next_page = 'supervisor'
        else:
            self.next_page = 'index'

        return super().form_valid(form)
