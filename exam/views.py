from django.shortcuts import render, redirect, get_object_or_404
from .forms import SectionForm, QuestionForm, ScheduleExamForm, SignUpForm, ChoiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from .models import Question, Section, Exam, User, Choice
from django.http import HttpResponse
# Create your views here.


def signupchoice(request):
	if request.method == 'POST':
		if 'teacher' in request.POST:
			request.session['role'] = 3
			return redirect('signup')
		elif 'student' in request.POST:
			request.session['role'] = 2
			return redirect('signup')
	return render(request, 'exam/signupchoice.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        role = request.session['role']
        if form.is_valid():
            user = form.save()
            return render(request, "exam/login.html")
    else:
        form = SignUpForm()
    return render(request, 'exam/signup.html', {'form': form})



class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'exam/login.html'
	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username  = username, password = password)
		if user is not None and user.is_active:
			login(self.request, user)
			if user.role == 2:
				return redirect("student")
			elif user.role == 3:
				return redirect("index")
		else:
			return self.form_invalid(form)




def index(request):
	return render(request, "exam/index.html")

def choice(request):
	if request.method == "POST":
		choice_form = ChoiceForm(request.POST)
		if choice_form.is_valid():
			obj = Choice()
			obj.question =choice_form.cleaned_data['question']
			obj.choice = choice_form.cleaned_data['choice']
			print(obj.question)
			obj.save()
			# return redirect("choice")
	else:
		choice_form = ChoiceForm

	return render(request, "exam/choice.html", {"choice_form" : choice_form})
	# return render(request, "exam/index.html")


def question(request):
	if request.method == "POST":
		ques_form = QuestionForm(request.POST)
		if ques_form.is_valid():
			obj = Question()
			obj.section =ques_form.cleaned_data['section']
			obj.question = ques_form.cleaned_data['question']
			print(obj.question)
			obj.save()
			return render("choice")
	else:
		ques_form = QuestionForm

	return render(request, "exam/question.html", {"ques_form" : ques_form})



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
	question = Question.objects.all()
	choice = Choice.objects.all()
	return render(request, "exam/student_exam.html", {"question" : question, "exam":exam, "choice":choice})

