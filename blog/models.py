from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Tag(models.Model):
    """Post Tags"""
    title = models.CharField(max_length=50, verbose_name='Название Тега')
    slug = models.SlugField(max_length=255, verbose_name='Url_of_Tag', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ['title']


class Category(models.Model):
    """Post Categories"""
    title = models.CharField(max_length=255, verbose_name='Название Категории')
    slug = models.SlugField(max_length=255, verbose_name='Url_of_Category', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Post(models.Model):
    """Posts"""
    title = models.CharField(max_length=255, verbose_name='Название Поста')
    slug = models.SlugField(max_length=255, verbose_name='Url_of_Post', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время Создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время последнего Редактирования")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='get_category',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, related_name='get_tags')
    likes = models.ManyToManyField(User, blank=True, related_name="get_likes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты(ов)"
        ordering = ['-created_at']


class Comment(models.Model):
    """Post Comments"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="get_comments")
    name = models.CharField(max_length=50, verbose_name="Имя")
    comment = models.CharField(max_length=700, verbose_name="Коментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время последнего Редактирования")
    likes = models.ManyToManyField(User, blank=True, related_name="likes_comments")

    def __str__(self):
        return f'{self.name} - {self.comment}'

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
        ordering = ["name"]


class ReplyComment(models.Model):
    """Reply Comments"""
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="get_parent_comments")
    name = models.CharField(max_length=50, verbose_name="Имя_отвечающего")
    comment = models.CharField(max_length=700, verbose_name="Коментарий_отвечающего")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время последнего Редактирования")
    likes = models.ManyToManyField(User, blank=True, related_name="get_reply_comments_likes")

    def __str__(self):
        return f'{self.name} - {self.comment}'

    class Meta:
        verbose_name = "Ответный_Коментарий"
        verbose_name_plural = "Ответные_Коментарии"
        ordering = ["name"]
