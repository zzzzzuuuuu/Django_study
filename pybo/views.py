from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from django.http import HttpResponseNotAllowed
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# from django.http import HttpResponse #HttpResponse: 요청에 대한 응답을 할 때 사용 #필요없어져서 삭제

# def index(request): #매개변수 request는 HTTP의 요청 객체
#     return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")

def index(request):
    page = request.GET.get('page', '1')
    #GET 방식으로 호출된 url에서 page를 가져올 때 사용.
    question_list = Question.objects.order_by('-create_date') #작성일시 역순으로 정렬
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) #페이징객체. 해당 페이지의 데이터만 조회하도록(전체x)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context) #render함수: 파이썬 데이터를 템플릿에 적용하여 html로 반환.


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) #오류페이지 500메시지 대신 404메시지가 뜨도록
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # #question.answer_set: 질문에 대한 답변. 답변을 생성하기 위해.. (create..)
    # return redirect('pybo:detail', question_id=question.id)
    if request.method == "POST": #답변 등록은 post 방식만 사용됨.
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else: #get방식으로 요청할 경우 오류 발생
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request): #질문 등록하기 버튼을 누르면!
    # form = QuestionForm()
    # return render(request, 'pybo/question_form.html', {'form': form})
    if request.method == 'POST': #저장하기 버튼을 누르면.. action 디폴트값.. 이라는데 ..?
        form = QuestionForm(request.POST)
        if form.is_valid(): #폼이 유효하다면
            question = form.save(commit=False) #임시저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now() #실제 저장을 위해 작성일시를 설정한다.
            question.save() #데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)