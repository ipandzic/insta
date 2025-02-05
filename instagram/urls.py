"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.views import UserRegisterView
from core.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  PostListView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('profiles/', include(('accounts.urls', 'accounts'), namespace='profiles')),
    path('post/', include(('core.urls', 'core'), namespace='post')),
    path('api/post/', include(('core.api.urls', 'core-api'), namespace='post-api')),
    path('register/', UserRegisterView.as_view(), name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
