from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView

# index의 매개변수는 request(요청) or response(대답) ? 외워?
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_count'] = Post.objects.filter(category=None).count()

        return context

def categories_page(request, slug):
    if slug=="no-category":
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    context= {
        'category' : category,
        'categories' : Category.objects.all(),
        'post_list' : post_list,
        'no_category_count' : Post.objects.filter(category=category).count()
    }
    return render(request, 'blog/post_list.html', context)

def tag_page(request, slug):

    tag = Tag.objects.get(slug=slug)
    post_list = Post.post_set.all() # 다대 다라서 뭔가 다름...

    context= {
        'tag' : tag,
        'categories' : Category.objects.all(),
        'post_list' : post_list,
        'no_category_count' : Post.objects.filter(category=category).count()
    }
    return render(request, 'blog/post_list.html', context)



