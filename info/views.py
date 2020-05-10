from django.shortcuts import render
from django.http import HttpResponse


def news(request):
    return HttpResponse('The template displaying some details')
    # Just load an html template
