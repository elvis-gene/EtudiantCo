from django.shortcuts import render
from .models import Student
from django.http import HttpResponse


def home(request):
    # text = "Nous, etudiants congolais "

    return render(request, 'form/index.html')
