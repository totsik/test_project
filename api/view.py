from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Post, UserLike
from .serializers import PostSerializer


class PostModelView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=True, url_path='like', url_name='like-post')
    def like_post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        user_like = UserLike.objects.create(post=post, user=user)
        user_like.save()

        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_path='unlike', url_name='unlike-post')
    def unlike_post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        user_like = UserLike.objects.filter(post=post, user=user).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)