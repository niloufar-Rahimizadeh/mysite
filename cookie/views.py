from django.shortcuts import render
from .forms import CookieForm
from .models import Cookie
# Create your views here.
from django.contrib.auth.models import AbstractBaseUser

def create(request):
    if request.method == "POST":
        form = CookieForm(request.POST)
        if form.is_valid(): 
            form.save()
    return render(request, 'cookie/create.html')

def read(request):
    cookies = Cookie.objects.all()
    return render(request, {'cookies': cookies})

def update(request, cookieId):
    cookie = Cookie.objects.get(id=cookieId)
    if request.method == "POST":
        form = CookieForm(request.POST, request.FILES, instance=cookie)
        if form.is_valid():
            form.save()
    return render(request, 'cookie/update.html', {'cookie': cookie})


def delete(request, cookieId):
    pass


