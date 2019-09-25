from rest_framework import generics, permissions
from django.db.models import Q
from core.models import Post

from .pagination import StandardResultsPagination
from .serializers import PostModelSerializer

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

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


class PostActionsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, Delete or Modify Post.
    """
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
