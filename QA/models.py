from django.db import models
from django.contrib.auth.models import User
import datetime 

# Create your models here.


class Question(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=200)
    text = models.TextField()
    publish_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    text = models.TextField()
    publish_date = models.DateTimeField(default=datetime.datetime.now)




