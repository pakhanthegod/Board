from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, Div

from .models import Post, Comment

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'border rounded p-3'
        self.helper.layout = Layout(
            Div(
                Field('post_title', css_class='form-control'),
                css_class='form-group'
            ),
            Div(
                Field('post_text', css_class='form-control'),
                css_class='form-group'
            )
        )
        self.helper.layout.append(Submit('save', 'Создать'))

    class Meta:
        model = Post
        exclude = ['post_date']
        labels = {
            'post_title': 'Тема: ',
            'post_text': 'Текст: '
        }

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_class = 'border rounded p-3'
        self.helper.layout = Layout(
            Div(
                Field('comment_text', css_class='form-control'),
                css_class='form-group'
            ),
        )
        self.helper.layout.append(Submit('save', 'Отправить'))

    class Meta:
        model = Comment
        exclude = ['comment_date', 'post']
        labels = {
            'comment_text': 'Написать комментарий: '
        }