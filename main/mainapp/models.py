from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.http import JsonResponse


class Account(models.Model):
    first_name = models.CharField('Введите ваше имя', max_length=20)
    email_address = models.EmailField('Email')
    message = models.TextField('Введите сообщение', max_length=2000)

    def __str__(self):
        return "Имя пользователя: " + str(self.first_name) + "\nПочта:\n" + str(
            self.email_address) + "\nСообщение:\n" + str(
            self.message) + "\n"


def accountToDictionary(account):
    output = {"first_name": account.first_name,
              "email_address": account.email_address,
              "message": account.message}
    return output


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
