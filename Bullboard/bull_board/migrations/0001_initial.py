# Generated by Django 5.0.4 on 2024-05-11 13:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(max_length=20, unique=True)),
                ('text', models.TextField()),
                ('dateCreations', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хилы'), ('dd', 'ДД'), ('buyers', 'Торговцы'), ('gildemaster', 'Гилдмастеры'), ('quest', 'Квестгиверы'), ('smith', 'Кузнецы'), ('tanner', 'Кожевники'), ('potion', 'Зельевары'), ('spillmaster', 'Мастера заклинаний')], default='tank', max_length=12)),
                ('upload', models.FileField(upload_to='uploads/')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateCreations', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0)),
                ('commentArticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bull_board.article')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bull_board.article')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
