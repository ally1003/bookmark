from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete 각각의 페이지를 만들 수 있다면 굿
# List 먼저 만들기

# 클래스형 뷰(제네릭 뷰 이미 있는거 사용), 함수형 뷰(자유롭게 내가 만들기)
# 웹 페이지에 접속한다. => 페이지를 본다.
# url을 입력 => 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답(이 화면을 봄)

from django.views.generic.list import ListView # 컨트롤하고 클릭하면 목록 볼 수 있음
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')