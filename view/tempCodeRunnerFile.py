from django.contrib import admin
from django.urls import path
from view import views

urlpatterns = [
    path("/<no1>", views.readfiles , name='home/file1'),
    #path("file2", views.readfiles2 , name='file2'),
    #path("file3", views.readfiles3 , name='file3'),
    #path("file4", views.readfiles4, name='file4'),
    
]