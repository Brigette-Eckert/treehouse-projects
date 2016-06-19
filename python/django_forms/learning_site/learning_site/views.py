from django.shortcuts import render

from . import forms


def hello_world(request):
    return render(request, 'home.html')