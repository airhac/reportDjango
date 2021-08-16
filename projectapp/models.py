from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now_add=True)