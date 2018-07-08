from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    posts_list = Post.objects.all().order_by('-post_date')
    paginator = Paginator(posts_list, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'board/index.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('board:detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'board/detail.html', {'post': post, 'form': form})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('board:detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form': form})