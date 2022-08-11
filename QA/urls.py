from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home , name = "home"),
    path('questions/',views.questions , name = "questions"),
    path('question/<int:Qid>',views.question , name = "question"),
]