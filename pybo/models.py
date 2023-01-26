from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200) #제목 최대 200자. 글자수 제한 텍스트 CharField
    content = models.TextField() #글자수 제한 없는 텍스트 TextField
    create_date = models.DateTimeField() #날짜, 시간 관련은 DateTimeField

    def __str__(self): #id값 대신 제목으로 표시
       return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #해당 답변과 연결된 질문이 삭제될경우 답변도 삭제됨.
    content = models.TextField()
    create_date = models.DateTimeField()
