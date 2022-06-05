from django.core.exceptions import ValidationError
from django.forms import TextInput, EmailInput, Textarea, ModelForm
from .models import Account, Post, Comment
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'email_address', 'message']

    widgets = {
        "first_name": TextInput(attrs={'class': 'input1', 'placeholder': 'Ваше имя'}),
        "email_address": EmailInput(attrs={'class': 'input1', 'placeholder': 'Email'}),
        "message": Textarea(attrs={'class': 'textarea1', 'placeholder': 'Введите сообщение'})
    }


def print_form(self):
    return str(self) + "\n"


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            "name": TextInput(attrs={'class': 'input', 'placeholder': _('Ваше имя')}),
            "email": EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            "body": Textarea(attrs={'class': 'textarea', 'placeholder': _('Введите комментарий')})
        }