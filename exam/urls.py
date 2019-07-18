
from django.urls import path
from . import views
from .views import LoginView
urlpatterns = [
    path('question', views.question, name = "question"),
    path('choice', views.choice, name = "question"),
    path('section', views.section, name = "section"),
    path('student', views.student, name = "student"),
    path('student_exam/<int:pk>', views.student_exam, name = "student_exam"),
    path('schedule_exam', views.schedule_exam, name = "schedule_exam"),
    path('login/', LoginView.as_view(), name = "login"),
    path('index', views.index, name = "index"),
    path('', views.signupchoice, name = "signupchoice"),
    path('signup/', views.signup, name='signup'),
    



]