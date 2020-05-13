from django.shortcuts import render
from django.http import HttpResponse



def get_list(request):
    # return HttpResponse('The template displaying list of students will be called here')
    return render(request, 'students_list/list.html')

def expired_list(request):
    return HttpResponse('with expired passports')
