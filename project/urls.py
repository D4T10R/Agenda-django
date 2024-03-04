from django.contrib import admin
from django.urls import include, path

app_name = 'contact'

urlpatterns = [
    path('', include('contact.urls')), 
]
