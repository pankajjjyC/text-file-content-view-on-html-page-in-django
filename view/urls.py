from django.contrib import admin
from django.urls import path
from view import views

urlpatterns = [
    path("", views.readfiles , name='home/file1'),
    path("file1", views.readfiles , name='home/file1'),
    path("<no1>/<no2>", views.readfiles_ar , name='home/file1'),
    path("file1/<no1>/<no2>", views.readfiles_ar , name='home/file1'),
    path("file2", views.readfiles2 , name='file2'),
    path("file2/<no1>/<no2>", views.readfiles2_ar , name='home/file1'),
    path("file3", views.readfiles3 , name='file3'),
    path("file3/<no1>/<no2>", views.readfiles3_ar , name='home/file1'),
    path("file4", views.readfiles4, name='file4'),
    path("file4/<no1>/<no2>", views.readfiles4_ar , name='home/file1'),
    
]

