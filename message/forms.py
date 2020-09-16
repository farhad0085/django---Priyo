from django.forms import ModelForm
from .models import *

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['msg_body']
