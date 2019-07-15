from .models import Section, Question, Exam
from django import forms

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = "__all__"



class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = "__all__"


class ScheduleExamForm(forms.ModelForm):
	Section = forms.ModelMultipleChoiceField(queryset=Section.objects.all())
	class Meta:
		model = Exam
		fields = "__all__"