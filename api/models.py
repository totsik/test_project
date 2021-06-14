from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    body = models.TextField(default="")
    user = models.ForeignKey(
        to=User,
        related_name='user_post',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Post'

    def __str__(self):
        return 'ID: %s, Name: %s' % (self.id, self.name)


class UserLike(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        to=User,
        related_name='user_like',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        to=Post,
        related_name='post_like',
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'user_post_like'
        verbose_name = 'User like to post'
        verbose_name_plural = 'User like to post'
        unique_together = ('user', 'post')
