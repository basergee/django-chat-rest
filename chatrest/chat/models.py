from django.db import models
from django.contrib.auth.models import User


# Профиль пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='uploads/', blank=True)


class Chat(models.Model):
    DIALOG = 'D'
    GROUP = 'G'
    CHAT_TYPE_CHOICES = (
        (DIALOG, 'Личные сообщения'),
        (GROUP, 'Групповой чат')
    )

    type = models.CharField(
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    theme = models.CharField(max_length=256, blank=True)
    members = models.ManyToManyField(Profile)


# Сообщение в чате
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
