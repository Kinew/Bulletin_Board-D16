from django.db import models
from django.contrib.auth.models import User


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
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=8, choices=TYPE, default='tank')
    upload = models.FileField(upload_to='uploads/')


class UserResponse(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Advert(models.Model):
    heading = models.OneToOneField(Advert, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreations = models.DateTimeField(auto_now_add=True)
    images = models.ImageField()



class Comment(models.Model):
    commentArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreations = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()