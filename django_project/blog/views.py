from django.shortcuts import render
from .models import Post


# index의 매개변수는 request(요청) or response(대답) ? 외워?
def index(request):
    # 사용자의 요청을 받아서 이런일 저런일을 ...
    posts = Post.objects.all().order_by('-pk')

    return render(
        request, 'blog/index.html', {'posts': posts})
