from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('', ideas_list, name='list'),
    path('<int:pk>/', ideas_detail, name='detail'),
    path('<int:pk>/toggle_star/', toggle_star, name='toggle_star'),
    path('create/', ideas_create, name="create"),
    path('<int:pk>/delete/', ideas_delete),
    path('<int:pk>/update/', ideas_update),
    path('<int:pk>/adjust_interest/', adjust_interest, name='adjust_interest'),
]
