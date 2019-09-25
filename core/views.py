from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from django.db.models import Q

from .forms import PostModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Post


class PostCreateView(FormUserNeededMixin, CreateView):
    form_class = PostModelForm
    template_name = "core/create_view.html"


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = "core/detail_view.html"


class PostListView(LoginRequiredMixin, ListView):
    
    #template_name = "core/post_list.html"

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     im_following = self.request.user.profile.get_following()
    #     qs1 = Post.objects.filter(user__in=im_following)
    #     qs2 = Post.objects.filter(user=self.request.user)
    #     qs = (qs1 | qs2).distinct()
    #     return qs

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) | 
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["create_form"] = PostModelForm()
        context["create_url"] = reverse_lazy("core:create")
        return context


class PublicPostListView(ListView):
    queryset = Post.objects.all()
    template_name = "core/public_post_list.html"


class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Post.objects.all()
    template_name = "core/update_view.html"
    form_class = PostModelForm
    success_url = "/core/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    queryset = Post.objects.all()
    template_name = "core/delete_confirm.html"
    success_url = reverse_lazy('core:list')
