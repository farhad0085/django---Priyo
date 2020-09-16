from django.forms import ModelForm
from .models import *

class PhotoPostForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']