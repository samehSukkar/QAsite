from urllib import request
from django.http import HttpResponse 
from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from .models import Question , Answer
from .forms import AnswerForm , QuestionForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return HttpResponse("hello")





def questions(request):

    all_questions  = Question.objects.all()
    return render(request ,  'QA\\questions.html',{ 'questions' : all_questions})




def question(request , Qid):

    q = get_object_or_404(Question , pk = Qid)

    if request.method == 'POST':
        
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = q
            answer.save()

 
    form = AnswerForm()
    answers = q.answer_set.all()
   
    return render(request ,  'QA\\question.html',{ 'question' : q ,'answers' : answers ,'form' : form})

    

@login_required
def add_question(request):

    form = QuestionForm(request.POST)

    if request.method == 'POST':
            
            if form.is_valid():
               question = form.save(commit=False)
               question.author = request.user
               question.save()

               return redirect('questions/')

        
    
    return render(request ,  'QA\\add_question.html', { 'form' : form})

