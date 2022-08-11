from django.contrib import admin
from .models import Question , Answer
# Register your models here.




class QuestionAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'publish_date')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','author')


admin.site.register(Answer,AnswerAdmin)
admin.site.register(Question,QuestionAdmin)
