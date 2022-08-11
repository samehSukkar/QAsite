from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
# Create your views here.


def home(request):
    return HttpResponse("hello")





def questions(request):

    all_questions  = Question.objects.all()
    return render(request ,  'QA\\questions.html',{ 'questions' : all_questions})




def question(request , Qid):

    q = Question.objects.filter(pk = Qid)
    return render(request ,  'QA\\question.html',{ 'question' : q})
