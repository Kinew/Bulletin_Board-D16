from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spillmaster', 'Мастера заклинаний'),
    )


    author = models.OneToOneField(User, on_delete=models.CASCADE)
    dateCreations = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    text = RichTextUploadingField()
    category = models.CharField(max_length=12, choices=TYPE, default='tank')


class Comment(models.Model):
    commentArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreations = models.DateTimeField(auto_now_add=True)
