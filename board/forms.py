from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .models import Post, Comment


class PostCreate(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'captcha')
        labels = {
            'title': _('Тема'),
            'text': _('Текст'),
            'image': _('Изображение'),
            'captcha': _('Подтвержение'),
        }


class CommentCreate(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Comment
        fields = ('text', 'image', 'captcha')
        labels = {
            'text': _('Текст'),
            'image': _('Изображение'),
            'captcha': _('Подтвержение'),
        }
