from django.urls import path

from .views import PostListAPIView, PostCreateAPIView, PostActionsAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('actions/<int:pk>/', PostActionsAPIView.as_view(), name="post-actions")
]
