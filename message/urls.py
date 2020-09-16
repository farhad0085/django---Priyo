from django.urls import path
from . import views as users_view

urlpatterns = [
    path('message/<username>/', users_view.message, name='message'),
    path('inbox/', users_view.inbox, name='inbox'),
]
