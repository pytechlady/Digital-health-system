from django.urls import path

import doctor
from . import views
# from doctor.views import dashboard

urlpatterns = [
    path('register',views.registration, name='register'),
    path('appointment', views.appointment, name = 'appointment'),
    path('medical-records', views.medical_records, name='medical_records'),
    path('dashboard/', views.dashboard, name='patient_dashboard'),
    # path('pie-chart/', views.pie_chart, name='pie-chart'),
   
]