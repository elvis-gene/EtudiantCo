from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('form.urls')),
    path('info/', include('info.urls')),
    path('students_list/', include('students_list.urls')),
    path('admin/', admin.site.urls),
]
