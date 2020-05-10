from django.shortcuts import render
from django.http import HttpResponse



def get_list(request):
    return HttpResponse('The template displaying list of students will be called here')

def expired_list(request):
    return HttpResponse('with expired passports')
