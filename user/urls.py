from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('all_user/', views.see_user, name='all_user'),
]
