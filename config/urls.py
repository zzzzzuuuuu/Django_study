from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

# from pybo import views #프로젝트 성격의 파일이므로 프로젝트 성격의 url 매핑만 추가되어야 함. 더이상 필요하지 않으므로 삭제

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pybo/', views.index), #pybo/ url이 요청되면 views.index(=views.py의 index 함수)를 호출하라는 매핑
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'), #'/'에 해당되는 path
]
