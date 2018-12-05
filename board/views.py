import re

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist

from .models import Post, Comment, Thread
from .forms import PostCreate, CommentCreate


class ThreadList(ListView):
    model = Thread
    template_name = 'board/index.html'
    context_object_name = 'threads'


class PostList(ListView):
    template_name = 'board/thread.html'
    context_object_name = 'posts'

    def get_queryset(self):
        thread = get_object_or_404(Thread, name=self.kwargs['thread'])
        return Post.objects.filter(thread=thread)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = self.kwargs['thread']
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        post.view_count += 1
        post.save()
        context['form'] = CommentCreate()
        return context


class PostCreateView(CreateView):
    template_name = 'board/post_create.html'
    form_class = PostCreate

    def form_valid(self, form):
        form_save = form.save(commit=False)
        thread = get_object_or_404(Thread, name=self.kwargs['thread'])
        form_save.thread = thread
        form_save.save()
        return super().form_valid(form_save)

    def get_success_url(self):
        return reverse('board:thread_posts', kwargs={'thread': self.kwargs['thread']})


class CommentCreateView(View):
    form_class = CommentCreate
    template_name = 'board/post.html'

    def post(self, request, *args, **kwargs):
        thread = self.kwargs['thread']
        post_id = self.kwargs['pk']
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                pattern = r'(>>\d+)'
                replies_to = re.findall(pattern, comment.text)
                post = Post.objects.get(pk=post_id)
                comment.post = post
                comment.save()
                for reply in replies_to:
                    try:
                        trunc_reply = int(reply[2:])
                        obj = Comment.objects.get(pk=trunc_reply, post=post)
                        if obj:
                            comment.reply_to.add(obj)
                            comment.text = comment.text.replace(reply, f'<a href="#{trunc_reply}">&gt;&gt;{trunc_reply}</a>')
                    except ObjectDoesNotExist:
                        pass
                comment.save()
            except ObjectDoesNotExist:
                pass
            form.save_m2m()
            return redirect('board:post', thread=thread, pk=post_id)
        return render(request, self.template_name, {'form': form, 'thread': thread, 'pk': post_id})
