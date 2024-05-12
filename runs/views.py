from django.shortcuts import render
import requests
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def start(requet):
    g = requests.get("http://192.168.0.172/sock1/start")
    return render(requet, 'wait.html')