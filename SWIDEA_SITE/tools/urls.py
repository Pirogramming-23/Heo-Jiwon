from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'tools'

urlpatterns = [
    path('', tools_list, name='main'),
    path('<int:pk>/', tools_detail, name='detail'),
    path('create/', tools_create, name='create'),
    path('<int:pk>/delete/', tools_delete),
    path('<int:pk>/update/', tools_update),
]
