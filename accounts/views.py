from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from rest_framework import generics, permissions
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from .serializers import UserModelSerializer

from .forms import UserRegisterForm
from .models import User

User = get_user_model()


class UserRegisterView(FormView):
    template_name = "accounts/user_register_form.html"
    form_class = UserRegisterForm
    success_url = "/login"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create(username=username)
        new_user.set_password(password)
        new_user.save()
        return super(UserRegisterView, self).form_valid(form)


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(
            User,
            username__iexact=self.kwargs.get("username")
            )

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context["following"] = following
        context["recommended"] = UserProfile.objects.recommended(self.request.user)
        return context


class UserFollowView(View):

    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated:
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = User.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) | 
                Q(user__username__icontains=query)
            )
        return qs


class UserActionsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, Delete or Modify User.
    """
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
