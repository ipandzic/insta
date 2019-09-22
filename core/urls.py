from django.urls import path
from django.views.generic.base import RedirectView

from core import views

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('list/', views.PostListView.as_view(), name='list'),
    path('public/', views.PublicPostListView.as_view(), name='public'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
