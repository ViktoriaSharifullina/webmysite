from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register, TranslationOptions
from .models import *
from modeltranslation.admin import TranslationAdmin


@register(Account)
class AccountTranslationOptions(TranslationOptions):
    fields = ('first_name', 'message')


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


