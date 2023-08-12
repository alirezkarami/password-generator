from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('passwords/', views.read, name='passwords'),
    path('update/', views.update, name='update'),
]