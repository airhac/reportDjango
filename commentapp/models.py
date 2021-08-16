from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    #개시글의 id 어떤 게시글인지(서버단에서 확인 해야한다)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    #댓글 작성자가 누구인지
    content = models.TextField(null=False)
    #댓글의 내용이 무엇인지
    created_at = models.DateTimeField(auto_now=True)
    #댓글이 언제 생성되는지(자동생성)