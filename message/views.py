from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inbox(request):
    users = User.objects.exclude(username=request.user.username)
    try:
        last_message = Message.objects.filter(Q(msg_from=request.user) | Q(msg_to=request.user)).last()
        user = last_message.msg_from.username if request.user.username != last_message.msg_from.username else last_message.msg_to.username
        return redirect('message', user)
    except:
        context = {
            "users": users
        }
        return render(request, 'message/message.html', context)

def message(request, username):
    if username == request.user.username:
        return redirect('index')
    try:
        user = User.objects.get(username=username)
    except:
        return redirect('index')
    
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.msg_from = request.user
            message.msg_to = user
            form.save()
            return redirect('message', username)

    messages = Message.objects.filter(
                                    (Q(msg_to=request.user) & Q(msg_from=user)) |
                                    (Q(msg_from=request.user) & Q(msg_to=user))
                                ).order_by('id')
    try:
        last_message_id = "messageId-" + str(messages.last().id)
    except:
        last_message_id = "messageId-0"
    users = User.objects.exclude(username=request.user.username)
    context = {
        "form": form,
        "messages": messages,
        "username": username,
        "users": users,
        "last_message_id": last_message_id
    }
    return render(request, 'message/message.html', context)