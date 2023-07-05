from django.shortcuts import render,redirect
from patients.forms import AccountAuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages, auth
from patients.models import Appointment
from patients.models import PatientsRecords
from patients.views import appointment


def dashboard(request):
    return render(request, 'doctor_dashboard.html')

def appoint(request):
    if request.user.is_authenticated:
        appointments = Appointment.objects.order_by('username')
        data={
            'appointments' : appointments,
        }
        return render(request, 'doctor_appointment.html', data)
    else:
        messages.error(request, "please Login")
        return redirect('login')
    

def record(request):
    if request.user.is_authenticated:
        records = PatientsRecords.objects.order_by('username')
        data={
            'records' : records,
        }
        return render(request, 'doctor_record.html', data)
    else:
        messages.error(request, "please Login")
        return redirect('login')