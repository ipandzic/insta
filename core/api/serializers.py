from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from core.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    timesince = serializers.SerializerMethodField()
    date_display = serializers.SerializerMethodField()

    def perform_create(self, serializer):
        serializers.save(user=self.request.user)

    class Meta:
        model = Post
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
