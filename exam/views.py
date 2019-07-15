from django.shortcuts import render, redirect, get_object_or_404
from .forms import SectionForm, QuestionForm, ScheduleExamForm
from .models import Question, Section, Exam
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, "exam/index.html")
def question(request):
	if request.method == "POST":
		ques_form = QuestionForm(request.POST)
		if ques_form.is_valid():
			obj = Question()
			obj.section =ques_form.cleaned_data['section']
			obj.question = ques_form.cleaned_data['question']
			print(obj.question)
			obj.save()
			return redirect("index")
	else:
		ques_form = QuestionForm

	return render(request, "exam/question.html", {"ques_form" : ques_form})
	# return render(request, "exam/index.html")


def section(request):
	if request.method == "POST":
		sec_form = SectionForm(request.POST)
		if sec_form.is_valid():
			obj = Section()
			obj.section =sec_form.cleaned_data['section']
			obj.save()
			return redirect("index")
	else:
		sec_form = SectionForm
	return render(request, "exam/section.html", {"sec_form" : sec_form})
	# return render(request, "exam/index.html")

def schedule_exam(request):
	if request.method == "POST":
		form = ScheduleExamForm(request.POST)
		if form.is_valid():
			obj = Exam()
			obj.name =ques_form.cleaned_data['name']
			obj.start_date = ques_form.cleaned_data['start_date']
			obj.duration = ques_form.cleaned_data['duration']
			obj.section = ques_form.cleaned_data['section']
			
			obj.save()
			return redirect("index")
	else:
		form = ScheduleExamForm

	return render(request, "exam/question.html", {"form" : form})



def student(request):
	exam = Exam.objects.all()
	return render(request, "exam/student.html", {"exam" : exam})

def student_exam(request, pk):
	exam = get_object_or_404(Exam, pk = pk)
	return render(request, "exam/student_exam.html", {"exam" : exam})

