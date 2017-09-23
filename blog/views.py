from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Post #이 파일이 있는 디렉토리와 같은 디렉토리에 있는 models라서 '.'models
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    # 여기에 filter()를 하면 리스트가 필터링돼서 뜨니까 그냥 all()로 하ㅁ
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #지금저장하지말고
            post.author = request.user
            post.published_date = timezone.now()
            post.save() #이제 저장해라
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)#인스턴스=실제값이있는것
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
