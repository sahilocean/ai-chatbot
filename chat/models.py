from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.username}" f"({self.id})"


class ChatMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_history")
    message = models.TextField()
    reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} - {self.timestamp}" if self.author.username else self.author.email
