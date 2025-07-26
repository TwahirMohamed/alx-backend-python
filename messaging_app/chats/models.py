from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )

    user_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest' )
    created_at = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    USERNAME_FIELD = 'username'


    def __str__(self):
        return f"{self.username} {self.role}"


class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField(max_length=500)
    sent_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Message:{self.message_body} Sent at{self.sent_at} from{self.sender_id}"

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='conversations' )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Conversation {self.conversation_id}from{self.participants_id}"