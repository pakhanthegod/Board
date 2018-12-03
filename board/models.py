from django.db import models
from django.utils import timezone
from django.urls import reverse


class Thread(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('board:thread_posts', kwargs={'thread': self.name})

    def __str__(self):
        return self.name


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts', null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255, null=True, blank=True)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        return reverse('board:post', kwargs={'thread': self.thread, 'pk': self.id})
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    reply_to = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='replies')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=timezone.now)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return str(self.pk)