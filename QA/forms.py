from django import forms
from .models import Answer , Question



class AnswerForm (forms.ModelForm):
    class Meta: 
        model = Answer
        fields = ['text',]
     

class QuestionForm (forms.ModelForm):
    class Meta: 
        model = Question
        fields = ['title','text']
     
