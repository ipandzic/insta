from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('actions/<int:pk>/', views.UserActionsAPIView.as_view(), name="user-actions"),
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
    path('<str:username>/follow/', views.UserFollowView.as_view(), name='follow')
]
