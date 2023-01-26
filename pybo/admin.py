from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin): #Question모델에 세부 기능을 추가할 클래스
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
#admin.site.register로 Question, ... 모델 등록
