from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelform_factory
from .models import Student
from phonenumber_field.widgets import PhoneNumberPrefixWidget, PhoneNumberInternationalFallbackWidget
from django import forms
from django.urls import reverse


StudentForm = modelform_factory(Student, exclude=['total'],
    widgets={'phone_number': PhoneNumberInternationalFallbackWidget(region='ZA', attrs={'pattern': '[0-9]+'}),
             'province': forms.Select(),
             'visa_expiry_date': forms.SelectDateWidget()})

def home(request):
    form = StudentForm()
    return render(request, 'form/index.html', {'form': form})


def process_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() # Students is created here
            return HttpResponseRedirect(reverse('students_list:get_list'))
    else:
        form = StudentForm()
    return render(request, 'form/index.html', {'form': form})
