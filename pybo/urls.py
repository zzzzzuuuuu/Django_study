from django.urls import path
from . import views

app_name = 'pybo' # 서로 다른 앱에서 동일한 url 별칭 중복을 막기위함이라는데 난 이해를 못했어요

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]