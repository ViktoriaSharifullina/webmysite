from django.contrib import admin
from .models import Account, Post, Comment
from modeltranslation.admin import TranslationAdmin


@admin.register(Account)
class AccountAdmin(TranslationAdmin):
    pass


@admin.register(Post)
class AccountAdmin(TranslationAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)
