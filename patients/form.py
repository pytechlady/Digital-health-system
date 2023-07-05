from .models import PatientsRecords, Appointment
from django import forms


class PatientsForm(forms.ModelForm):
    
    class Meta:
        model = PatientsRecords
        fields = ['gender', 'address', 'age', 'marital_status', 'phone_number', 'occupation', 'allergies', 'recent_diagnosis', 'sport_participation', 'sport_participation', 'sleep_routine', 'smoke_drink', 'self_medication' ]

class AppointmentForm(forms.ModelForm):
       class Meta:
        model = Appointment
        fields = ['service', 'time', 'notes']