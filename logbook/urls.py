from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # path('login/', LoginView.as_view(template_name="login.html", next_page="student"), name="login"),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html",next_page="index"), name="logout"),

    path('', Homepage.as_view(), name="index"),
    path('create-daily-report/', CreateDailyReport.as_view(), name="daily"),
    path('create-weekly-report/', CreateWeeklyReport.as_view(), name="weekly"),
    path('create-arival-note/', CreateArivalNote.as_view(), name="arivalnote"),
    path('create-recommendation/', CreateRecommendation.as_view(), name="recommendation"),

    path('student/', StudentView.as_view(), name="student"),
    path('supervisor/', SupervisorView.as_view(), name="supervisor"),
    path('weeklyreport/', WeeklyReportView.as_view(), name="weeklyreport"),
    path('dailyreport/', DailyReportView.as_view(), name="dailyreport"),
    path('arival-note/', ArivalNoteView.as_view(), name="arival_note"),

    # Registration views
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),


]
