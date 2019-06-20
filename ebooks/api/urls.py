from django.urls import path
from ebooks.api import views

urlpatterns = [
    path('ebooks/', views.EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('ebooks/<int:pk>/', views.EbookDetailAPIView.as_view(), name='ebook-detail'),
    path('ebooks/<int:ebook_pk>/review/', views.ReviewCreateAPIView.as_view(), name='ebook-review'),

    path('reviews/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='review-Detail'),
]
