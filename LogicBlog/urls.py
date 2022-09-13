from django.contrib import admin
from django.urls import path
from . import views
from .views import DetailedView, NewsView, CreatePost

urlpatterns = [
    path('', views.home, name="home"),
    # path('news/', views.news, name="news"),
    path('news/', NewsView.as_view(), name="news"),
    path('news/<int:pk>', DetailedView.as_view(), name="news-detail"),
    path('add_post/', CreatePost.as_view(), name="addpost")
]