from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author': 'James',
    'title': 'Blog post 1',
    'content': 'First post content',
    'date_posted': '22 Aug, 2019'
  },
  {
    'author': 'Kelly',
    'title': 'Blog post 2',
    'content': 'Second post content',
    'date_posted': '23 Aug, 2019'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})