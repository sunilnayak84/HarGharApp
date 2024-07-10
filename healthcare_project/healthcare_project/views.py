from django.http import HttpResponse
from django.db import models

def home(request):
    return HttpResponse("Welcome to the Modular Healthcare App")
