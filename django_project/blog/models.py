from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Post 모델의 타이틀이 대표가 됨
    def __str__(self): #string 내장함수 오버라이딩
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

