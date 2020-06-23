from django.shortcuts import render
from django.http import HttpResponse
from form.models import Student


def get_list(request):
    students = Student.objects.all()
    students_count = len(students)
    return render(request, 'students_list/list.html',
                            {'students': students, 'students_count': students_count})

# TODO:
def expired_list(request):
    return HttpResponse('with expired passports')
