from django.urls import path
from . import views as photo_views

urlpatterns = [
    path('', photo_views.index, name='index'),
]
