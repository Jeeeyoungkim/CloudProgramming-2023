from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# cascade -> 사용자 탈퇴하면 글 지워짐
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    #Post 모델의 타이틀이 대표가 됨
    def __str__(self): #string 내장함수 오버라이딩
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

