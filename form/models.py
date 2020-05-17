from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# This will allow me to count the number of students
students_count = 0

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

# Add help texts
class Student(models.Model):
    first_name = models.CharField(max_length=50, help_text='Veuillez entrer votre numero de telephone.')
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    # phone_number_country_code = PhoneNumberField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    province = models.CharField(choices = provinces_list, default=1, max_length=15)
    zip_code = models.IntegerField()
    institution = models.CharField(max_length=100)
    visa_expiry_date = models.DateField('expiry date')


    def __str__(self):
        return '{} {}'.format(self.surname, self.first_name)
