from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

def home(request):
   return render(request, "index.html", {})

def news(request):
    return render(request, "news.html", {})

class NewsView(ListView):
    model = Post
    template_name = 'news.html'

class DetailedView(DetailView):
    model = Post
    template_name = 'news_details.html'

class CreatePost(CreateView):
    model = Post
    template_name =  'create_post.html'
    fields = '__all__'