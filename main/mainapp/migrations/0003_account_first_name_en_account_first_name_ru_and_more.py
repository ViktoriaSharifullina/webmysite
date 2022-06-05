# Generated by Django 4.0.4 on 2022-05-31 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='first_name_en',
            field=models.CharField(max_length=20, null=True, verbose_name='Введите ваше имя'),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name_ru',
            field=models.CharField(max_length=20, null=True, verbose_name='Введите ваше имя'),
        ),
        migrations.AddField(
            model_name='account',
            name='message_en',
            field=models.TextField(max_length=2000, null=True, verbose_name='Введите сообщение'),
        ),
        migrations.AddField(
            model_name='account',
            name='message_ru',
            field=models.TextField(max_length=2000, null=True, verbose_name='Введите сообщение'),
        ),
        migrations.AddField(
            model_name='comment',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='name_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='name_ru',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_en',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body_ru',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(db_index=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(db_index=True, max_length=150, null=True),
        ),
    ]
