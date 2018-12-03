from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Post, Comment


class PostCreate(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        labels = {
            'title': _('Тема'),
            'text': _('Текст'),
            'image': _('Изображение')
        }


class CommentCreate(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'image')
        labels = {
            'text': _('Текст'),
            'image': _('Изображение')
        }
