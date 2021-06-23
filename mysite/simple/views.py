from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

@login_required
def home(request):
    user = User.objects.get(pk = request.user.id)
    users = User.objects.exclude(pk=request.user.id)
    return render(request, 'simple/index.html', {"user": user, "users": users})

@login_required
def messages(request, user_id):
    user = User.objects.get(pk = user_id)
    messages = models.Message.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    #if request.user.id != user_id:
    #    return redirect('/')
    #else:
    #    user = User.objects.get(pk = user_id)
    #    return render(request, 'simple/messages.html', {"user": user})
    return render(request, 'simple/messages.html', {"user": user, "messages": messages})

@login_required
def send_message(request):
    receiver = User.objects.get(username = request.POST.get('to'))
    models.Message.objects.create(sender = request.user, receiver = receiver, content=request.POST.get('content'))
    return redirect('/')

@login_required
def search(request):
    user = request.user.id
    sender_raw = User.objects.get(username=request.POST.get('query'))
    sender = sender_raw.id
    query = models.Message.objects.raw('SELECT * FROM simple_message WHERE sender_id = %s AND receiver_id = %s' % (user, sender))
    messages = [m for m in query]
    return render(request, 'simple/messages.html', {'user': user, "messages": messages})

