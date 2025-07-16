from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ideas_list),
    path('<int:pk>/', ideas_detail),
]
