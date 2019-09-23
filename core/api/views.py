from rest_framework import generics

from core.models import Post

from .pagination import StandardResultsPagination
from .serializers import PostModelSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        im_following = self.request.user.profile.get_following()
        qs1 = Post.objects.filter(user__in=im_following)
        qs2 = Post.objects.filter(user=self.request.user)
        qs = (qs1 | qs2)
        return qs
