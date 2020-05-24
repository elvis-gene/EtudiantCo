from django import template
from datetime import datetime

register = template.Library()

@register.filter
def get_fullname(student):
    return student.surname + ' ' + student.first_name


@register.filter
def remainder_check(student):
    return student.id % 2 == 0


@register.filter
def date_formater(student):
    date_input =  student.visa_expiry_date.strftime('%d %m %y')
    date = datetime.strptime(date_input, '%d %m %y')
    return date.strftime('%d-%m-%y')


@register.filter
def capitalize_uni(student):
    return student.institution.upper()
