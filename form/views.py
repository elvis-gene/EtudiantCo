from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


def home(request):
    return render(request, 'form/index.html')


def process_form(request):
    return HttpResponse("Merci pour l'enregistrement")
