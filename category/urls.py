from django.urls import path
from . import views


urlpatterns = [
    path('send/', views.send, name='send'),
    path('view/', views.view ,name='view')
]

