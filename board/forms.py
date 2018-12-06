from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, ButtonHolder, Submit
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Создать пост',
                'title',
                'text',
                'image',
                'captcha',
            ),
            ButtonHolder(
                Submit('submit', 'Создать пост', css_class='btn btn-default')
            )
        )


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Создать комментарий',
                'text',
                'image',
                'captcha',
            ),
            ButtonHolder(
                Submit('submit', 'Ответить', css_class='btn btn-default')
            )
        )
