from django.contrib import messages
from django.contrib.auth.decorators import login_required  # 로그인이 필요함
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm, AnswerForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request): #질문 등록하기 버튼을 누르면!
    # form = QuestionForm()
    # return render(request, 'pybo/question_form.html', {'form': form})
    if request.method == 'POST': #저장하기 버튼을 누르면.. action 디폴트값.. 이라는데 ..?
        form = QuestionForm(request.POST)
        if form.is_valid(): #폼이 유효하다면
            question = form.save(commit=False) #임시저장하여 question 객체를 리턴받는다.
            question.author = request.user #author 속성에 로그인 계정 저장
            question.create_date = timezone.now() #실제 저장을 위해 작성일시를 설정한다.
            question.save() #데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST": #수정된 내용을 반영하는 경우
        form = QuestionForm(request.POST, instance=question) #request.POST 값으로 덮어쓰라는 의미
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now() #수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else: #GET방식
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')