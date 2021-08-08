from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True )
    #user 객체에서 article을 접근할때 related_name을 사용한다.

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False) # 이미지를 항상 넣도록 한다.
    content = models.TextField(null=True)

    create_at = models.DateField(auto_now_add=True, null=True)
    #자동으로 객체가 생성되었을떄 그 시간이 저장된다.