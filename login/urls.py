from django.urls import path
from . import views

urlpatterns = [
    path('', views.mylogin, name='mylogin'),
    path('home/', views.home, name='home'),
]
