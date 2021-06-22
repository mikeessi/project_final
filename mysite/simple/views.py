from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    user = User.objects.get(pk = request.user.id)
    return render(request, 'simple/index.html', {"user": user})

@login_required
def profile(request, user_id):
    user = User.objects.get(pk = user_id)
    #if request.user.id != user_id:
    #    return redirect('/')
    #else:
    #    user = User.objects.get(pk = user_id)
    #    return render(request, 'simple/profile.html', {"user": user})
    return render(request, 'simple/profile.html', {"user": user})
