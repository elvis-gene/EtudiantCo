from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Could also use a CharField and provide the options in the HTML.
provinces_list = (
    ('1', 'Eastern Cape'),
    ('2', 'Free State'),
    ('3', 'Gauteng'),
    ('4', 'KwaZulu-Natal'),
    ('5', 'Limpopo'),
    ('6', 'Mpumalanga'),
    ('7', 'Nothern Cape'),
    ('8', 'North West'),
    ('9', 'Western Cape'),
)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.CharField(choices = provinces_list, default=1, max_length=15)
    zip_code = models.IntegerField()
    institution = models.CharField(max_length=100)
    visa_expiry_date = models.DateField('expiry date')
    total = models.IntegerField()


    def __str__(self):
        return '{} {}'.format(self.surname, self.first_name)



# No need to use this. Will use the Django built-in function
    # def __init__(self, first_name, surname, institution, city, visa_expiry_date):
    #     models.Model.__init__(self)
    #     self.first_name = first_name
    #     self.surname = surname
    #     self.institution = institution
    #     self.city = city
    #     self.visa_expiry_date = visa_expiry_date
