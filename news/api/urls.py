from django.urls import path
from news.api import views

urlpatterns = [
    path('articles/', views.ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>/', views.ArticleDetailAPIView.as_view(), name='article=detail'),
]
