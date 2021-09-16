# 앱 이름에 urls.py 생성후 작업

from django.urls import path
from .views import *

urlpatterns = [
    # ~0.1/bookmark/
    # path(url, 그 주소에 보여줄 뷰
    # 클래스형 뷰는 꼭 .as_view() 넣어야함 => 클래스뷰를 함수형 뷰로 바꾸는 것
    # name='list' 는 화면에 보여줄 템플릿에서 이 url을 어떻게 불러서 쓸꺼야?라는 패턴 이름
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    # pk는 프라이머리 키 int: 숫자값 str,int,슬러그 형태가 있음
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),

]