from django.urls import path
from . import views

app_name = 'info'
urlpatterns = [
    # info
    path('', views.news, name='news'),
]
