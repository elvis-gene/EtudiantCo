from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    visa_expiry_date = models.DateField('expiry date')
    total = models.IntegerField()


# No need to use this. Will use the Django built-in function
    # def __init__(self, first_name, surname, institution, city, visa_expiry_date):
    #     models.Model.__init__(self)
    #     self.first_name = first_name
    #     self.surname = surname
    #     self.institution = institution
    #     self.city = city
    #     self.visa_expiry_date = visa_expiry_date


    def __str__(self):
        return '{} {}'.format(self.surname, self.first_name)
