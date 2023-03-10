# Generated by Django 4.1.5 on 2023-01-12 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url_of_Category')),
            ],
            options={
                'verbose_name': 'Категория(ю)',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('comment', models.CharField(max_length=700, verbose_name='Коментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего Редактирования')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название Тега')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url_of_Tag')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя_отвечающего')),
                ('comment', models.CharField(max_length=700, verbose_name='Коментарий_отвечающего')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего Редактирования')),
                ('likes', models.ManyToManyField(blank=True, related_name='get_reply_comments_likes', to=settings.AUTH_USER_MODEL)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_parent_comments', to='blog.comment', verbose_name='Родительский Коментарий')),
            ],
            options={
                'verbose_name': 'Ответный_Коментарий',
                'verbose_name_plural': 'Ответные_Коментарии',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Поста')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url_of_Post')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время Создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего Редактирования')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_category', to='blog.category', verbose_name='Категория')),
                ('likes', models.ManyToManyField(blank=True, related_name='get_likes', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='get_tags', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты(ов)',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_comments', to='blog.post', verbose_name='Пост'),
        ),
    ]
