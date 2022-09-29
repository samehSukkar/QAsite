from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home , name = "home"),
    path('questions/',views.questions , name = "questions"),
    path('categories/',views.categories , name = "categories"),
    path('categories/<category_name>',views.category , name = "category"),
    path('question/<int:Qid>',views.question , name = "question"),
    path('add_question',views.add_question , name = "add_question"),
]

