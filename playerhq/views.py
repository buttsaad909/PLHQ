from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    return render(request, 'playerhq/index.html', {})

def about(request):
    return render(request, 'playerhq/about.html', {})