from django.urls import path

from .views import PostListAPIView, PostCreateAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
]
