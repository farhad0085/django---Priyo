from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    msg_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='msg_from')
    msg_to = models.ForeignKey(User, on_delete=models.CASCADE)
    msg_body = models.CharField(max_length=50000, blank=False)
    sent_time = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.msg_from} -> {self.msg_to}"
