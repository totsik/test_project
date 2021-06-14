from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, UserLike


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'name', 'body', 'user')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['likes'] = UserLike.objects.filter(post=instance).count()
        return data
