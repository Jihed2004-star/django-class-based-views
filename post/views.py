from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DeleteView
from django.views.generic import DetailView


# Create your views here.

class PostList(ListView):
  model=Post

class PostDetail(DetailView):
  model=Post

class PostCreate():
  pass


class PostDelete():
  pass

class PostUpdate():
  pass




