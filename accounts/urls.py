from django.urls import path

from accounts import views

urlpatterns = [
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
    path('<str:username>/follow/', views.UserFollowView.as_view(), name='follow')
]
