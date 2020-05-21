from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse
from django.forms import modelform_factory
from .models import Student
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django import forms
from django.views.generic.edit import CreateView


# Use SelectateWidget
# 'phone_number_country_code': PhonePrefixSelect(initial='ZA'),
StudentForm = modelform_factory(Student, exclude=['total'],
    widgets={'phone_number': PhoneNumberPrefixWidget(attrs={'pattern': '[0-9]+'}, initial='ZA'),
             'province': forms.Select(),
             'visa_expiry_date': forms.SelectDateWidget()})

def home(request):
    form = StudentForm()
    return render(request, 'form/index.html', {'form': form})


def process_form(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() # Student is created here
            # return redirect("") # Could redirect the user to the 'Etudiants' page
            return HttpResponse("Merci pour l'enregistrement")

    else:
        form = StudentForm()
    return render(request, 'form/index.html', {'form': form})

# Another way to replace the two methods above is to use a 'CreateView'
# Later not to allow someone to input date in the past
