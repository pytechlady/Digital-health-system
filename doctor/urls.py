from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name= 'doctor_dahboard'),
    path('medical-records/', views.record, name= 'record'),
    path('view-appointment/', views.appoint, name= 'appoint' )
]