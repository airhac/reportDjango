from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #이 프로파일의 주인이 누구 인지를 정해주는 객체 생성
    #이 프로파일과 User객체를 하나씩 연결 해준다는 뜻이다.
    #CASCADE는 연결된 User객체가 삭제 되었을때 같이 profile을 삭제 하도록한다는 의미입니다.
    image = models.ImageField(upload_to='profile/', null=True)
    #이미지가 어디에 저장 될 것인지 경로를 설정 media밑에 profile이라는 경로가 추가 될것이다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)