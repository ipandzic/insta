from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from core.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    timesince = serializers.SerializerMethodField()
    date_display = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'content',
            'date_display',
            'timesince'
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
