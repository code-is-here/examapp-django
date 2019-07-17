from .models import Section, Question, Exam, Choice
from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', )



class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = "__all__"



class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = "__all__"

class ChoiceForm(forms.ModelForm):
	class Meta:
		model = Choice
		fields = "__all__"


class ScheduleExamForm(forms.ModelForm):
	Section = forms.ModelMultipleChoiceField(queryset=Section.objects.all())
	class Meta:
		model = Exam
		fields = "__all__"