from django.urls import path
from django.contrib.auth import views as auth_views #django.contrib.auth 앱의 LoginView 사용.

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), #registration 디렉터리가 아닌 common 디렉터리에서 login.html 파일 참조
]