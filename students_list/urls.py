from django.urls import path
from . import views

app_name = 'students_list'
urlpatterns = [
    # list
    path('', views.get_list, name='get_list'),
    # TODO: list/expired
    path('list/expired/', views.expired_list, name='expired_list')
]
