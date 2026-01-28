from django.db import models
from core.models import BaseModel 
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Room(BaseModel):
    name = models.CharField(max_length=255, blank=True)
    participants = models.ManyToManyField(User, related_name="chat_rooms")

    def __str__(self):
        return self.name or f"Room {self.uid}"
    
class Message(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    content = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.sender} in {self.room}"
