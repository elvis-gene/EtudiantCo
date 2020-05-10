from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    visa_expiry_date = models.DateTimeField('expiry date')
    total = models.IntegerField()
