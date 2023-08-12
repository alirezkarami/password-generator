from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.send, name='send'),
    path('view/', views.view, name='view')
]
