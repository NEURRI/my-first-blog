from django.shortcuts import render
from django.utils import timezone
from .models import Post #이 파일이 있는 디렉토리와 같은 디렉토리에 있는 models라서 '.'models

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
