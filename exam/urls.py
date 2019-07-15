
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = "index"),
    path('question', views.question, name = "question"),
    path('section', views.section, name = "section"),
    path('student', views.student, name = "student"),
    path('student_exam/<int:pk>', views.student_exam, name = "student_exam"),
    path('schedule_exam', views.schedule_exam, name = "schedule_exam"),



]