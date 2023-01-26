from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta: #모델폼은 이너클래스인 Meta클래스가 반드시 필요함. (모델과 모델의 속성을 적음)
        model = Question #사용할 모델
        fields = ['subject', 'content'] #QuestionForm에서사용할 Question 모델의 속성
        # #부트스트랩 적용
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        #한글표시
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }