from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
    return render(request, 'registration/register.html')
