from django.db import models

# Create your models here.
class HelloWorld(models.Model):# Model클래스에서 기초적인 틀을 상속받습니다. 받은 것으로 우리가 원하는 새로운 클래스로 만듭니다.
    text = models.CharField(max_length=225,null=False)#null은 공벡 입니다.
