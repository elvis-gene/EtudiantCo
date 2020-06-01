"""
This class is not used
"""
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'surname', 'institution', 'city', 'visa_expiry_date')

        # As I'm going to use django-widget-tweaks, I can set the attributes in the template
        # widget ={
        #     'first_name': forms.TextInput(attrs={
        #         'required': True, 'class': 'form-control',
        #     })
        # }


# Class StudentForm(forms.ModelForm):
#         first_name = forms.CharField(max_length=50)
#         surname = models.CharField(max_length=50)
#         institution = models.CharField(max_length=100)
#         city = models.CharField(max_length=50)
#         visa_expiry_date = models.DateField('expiry date')
