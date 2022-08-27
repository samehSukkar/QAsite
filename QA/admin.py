from django.contrib import admin
from . import models
# Register your models here.




class QuestionAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'publish_date')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question','author')


admin.site.register(models.Answer,AnswerAdmin)
admin.site.register(models.Question,QuestionAdmin)
admin.site.register(models.Category)