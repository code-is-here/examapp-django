from django.contrib import admin
from .models import User, Choice,Section, Question, Exam
# Register your models here.
admin.site.register(User)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Exam)
