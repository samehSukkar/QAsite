from django.contrib import admin
from .models import Question , Answer
# Register your models here.


admin.site.register(Answer)


class QuestionAdmin(admin.ModelAdmin):
   
           list_display = ('title', 'publish_date')



admin.site.register(Question,QuestionAdmin)
