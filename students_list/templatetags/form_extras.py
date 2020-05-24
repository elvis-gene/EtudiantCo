from django import template
from datetime import datetime

register = template.Library()

@register.filter
def get_fullname(student):
    return student.first_name + ' ' + student.surname


@register.filter
def remainder_check(student):
    return student.id % 2 == 0


@register.filter
def date_formater(student):
    date_input =  student.visa_expiry_date.strftime('%d %m %y')
    date = datetime.strptime(date_input, '%d %m %y')
    return date.strftime('%d-%m-%y')
