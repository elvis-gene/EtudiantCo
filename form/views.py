from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.forms import modelform_factory
from .models import Student
from phonenumber_field.widgets import PhoneNumberPrefixWidget, PhonePrefixSelect
from django import forms


# Use SelectateWidget
 # 'phone_number': PhoneNumberPrefixWidget(initial='ZA'),
StudentForm = modelform_factory(Student, exclude=['total'],
    widgets={'phone_number_country_code': PhonePrefixSelect(initial='ZA'),
             'province': forms.Select})

def home(request):
    form = StudentForm()
    return render(request, 'form/index.html', {'form': form})


def process_form(request):
    return HttpResponse("Merci pour l'enregistrement")


# Another way to replace the two methods above is to use a 'CreateView'
