from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic

from RSATU1.models import Post


def index(request):
    # return HttpResponse("<h2>Главная</h2>")
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def post(reqest, pid):
    try:
        post = Post.objects.get(id=pid)
        tags = post.tag.all()
    except:
        return render(reqest, 'index.html')
    return render(reqest, 'post.html', {'post': post, 'tags': tags})


def tags(reqest, tagid):
    list = Post.objects.filter(tag=tagid)
    return render(reqest, 'tags.html', {'post_list': list})


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.all()
