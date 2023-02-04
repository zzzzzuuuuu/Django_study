from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question #부모디렉터리의 models.py 모듈을 import


def index(request):
    page = request.GET.get('page', '1')
    #GET 방식으로 호출된 url에서 page를 가져올 때 사용.
    kw = request.GET.get('kw', '') #검색어
    question_list = Question.objects.order_by('-create_date') #작성일시 역순으로 정렬
    if kw:
        question_list = question_list.filter( #filter 함수에서 모델 속성에 접근하기 위해서는 언더바 두개(__)를 이용하여 하위속성에 접근한다.

            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(answer__content__icontains=kw) | #답변 내용 검색
            Q(author__username__icontains=kw) | #질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) #답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page) #페이징객체. 해당 페이지의 데이터만 조회하도록(전체x)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context) #render함수: 파이썬 데이터를 템플릿에 적용하여 html로 반환.


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id) #오류페이지 500메시지 대신 404메시지가 뜨도록
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
