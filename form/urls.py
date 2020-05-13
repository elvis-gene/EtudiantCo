from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    # form
    path('', views.home, name='home'),
    path('enregistré', views.process_form, name='process_form'),
]
