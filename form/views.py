from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.forms import modelform_factory
from .models import Student


StudentForm = modelform_factory(Student, exclude=['total'])
def home(request):
    form = StudentForm()
    return render(request, 'form/index.html', {'form': form})


def process_form(request):
    return HttpResponse("Merci pour l'enregistrement")


# Another way to replace the two methods above is to use a 'CreateView'
