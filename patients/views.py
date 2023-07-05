from django.contrib import messages, auth
from .models import Appointment
from patients.models import PatientsRecords
from .form import PatientsForm, AppointmentForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from patients.forms import AccountAuthenticationForm, RegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import User



def registration(request):
    context= {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            patients = authenticate(email=email, password=raw_password)
            login(request, patients)
            return redirect('patient_dashboard')
        else:
            context['registration_form'] = form
    
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'signup.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

def log_in(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user and not user.is_staff:
                login(request, user)
                return redirect('patient_dashboard')
            elif user.is_staff:
                login(request, user)
                return redirect('doctor_dahboard')
                
            
    else:
        form = AccountAuthenticationForm()
    
    return render(request, 'login.html', {'form' : form})
         
# def home(request):
#     return render(request, 'index.html' )



"""Appointment Views"""
# @login_required(login_url='login')
def appointment(request ,*args):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        username = user.username
        
        
        email = user.email
        service = request.POST['service']
        time = request.POST['time']
        notes = request.POST['notes']
        appointment = Appointment.objects.create(username=user, email=email, service=service, time=time, notes=notes)
        messages.success(request, 'Your Appointment has been created successfully')
        appointment.save()
        return redirect('patient_dashboard')
    appoint = AppointmentForm()
    
    data = {
            "appoint": appoint
        }
    
    return render(request, 'appointment.html', data)
"""Appointment Views"""

def medical_records(request):
    if request.method == 'POST':
        
        user = User.objects.get(id=request.user.id)
        record = PatientsRecords.objects.filter(username=user).first()
        email = request.user.email       
        gender = request.POST['gender']
        address = request.POST['address']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        phone_number = request.POST['phone_number']
        occupation = request.POST['occupation']
        allergies = request.POST['allergies']
        recent_diagnosis = request.POST['recent_diagnosis']
        sport_participation = request.POST['sport_participation']
        sleep_routine = request.POST['sleep_routine']
        smoke_drink = request.POST['smoke_drink']
        self_medication = request.POST['self_medication']
        

        if request.user.is_authenticated:
            print("******", user, record, request.user.id)
            if record is not None:
                # record = PatientsRecords.objects.update(gender=gender, address=address, age=age, marital_status=marital_status, phone_number=phone_number, occupation=occupation, allergies=allergies, recent_diagnosis=recent_diagnosis, sport_participation=sport_participation, sleep_routine=sleep_routine, smoke_drink=smoke_drink, self_medication=self_medication)
                # return redirect('patient_dashboard')
                pass
            else:
                records = PatientsRecords.objects.create(username=user, email=email, gender=gender, address=address, age=age, marital_status=marital_status, phone_number=phone_number, occupation=occupation, allergies=allergies, recent_diagnosis=recent_diagnosis, sport_participation=sport_participation, sleep_routine=sleep_routine, smoke_drink=smoke_drink, self_medication=self_medication)
                messages.success(request, 'Medical Records added successfully')
                records.save()
                return redirect('patient_dashboard')
            
    p_form = PatientsForm()
    
    data = {
            "p_form": p_form,
            
        }
    
    return render(request, 'patient_record.html', data)



def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def display_graph(request):
    smoker = PatientsRecords.SMOKE_DRINK_CHOICES.objects.get()
    return render(request, '')

import pprint

def dashboard(request):
      
    recent_diagnosis = []
    sport_participation = []
    smoke_drink = []
    self_medication = []

    queryset = PatientsRecords.objects.all()

    for params in queryset:
        recent_diagnosis.append(params.recent_diagnosis)
        sport_participation.append(params.sport_participation)
        smoke_drink.append(params.smoke_drink)
        self_medication.append(params.self_medication)
    

    sickness = [ 'Malaria', 'Cholera', 'Cancer', 'Fever']
    sport_choices = [ 'No', 'Sometimes', 'Always']
    smoke_drink_option = ['Smokes', 'Drinks', 'Smokes and Drinks']
    self_med = ['No', 'Always']

    param_counter = {
        'Malaria' : 0,
        'Cholera' : 0,
        'Cancer' : 0,
        'Fever' : 0,
        'No': 0,
        'Sometimes': 0,
        'Always' : 0,
        'Smokes' : 0,
        'Drinks' : 0,
        'Smokes and Drinks' : 0,
        'Med_No' : 0,
        'Med_Always': 0
    }
    
    for params in recent_diagnosis:
        if params == sickness[0]:
            param_counter[sickness[0]] += 1
        if params == sickness[1]:
            param_counter[sickness[1]] += 1
        if params == sickness[2]:
            param_counter[sickness[2]] += 1
        else:
            param_counter[sickness[3]] += 1

    for params in sport_participation:
        if params == sport_choices[0]:
            param_counter[sport_choices[0]] += 1
        if params == sport_choices[1]:
            param_counter[sport_choices[1]] += 1
        if params == sport_choices[2]:
            param_counter[sport_choices[2]] += 1

    for params in smoke_drink:
        if params == smoke_drink_option[0]:
            param_counter[smoke_drink_option[0]] += 1
        if params == smoke_drink_option[1]:
            param_counter[smoke_drink_option[1]] += 1 
        if params == smoke_drink_option[2]:
            param_counter[smoke_drink_option[2]] += 1

    for params in self_med:
        if params == self_medication[0]:
            param_counter['Med_No'] += 1
        if params == self_medication[1]:
            param_counter['Med_Always'] += 1


    data_sickness = [
        param_counter['Malaria'],
        param_counter['Cholera'],
        param_counter['Cancer'],
        param_counter['Fever']
    ]

    data_sport_choices = [
        param_counter['No'],
        param_counter['Sometimes'],
        param_counter['Always']
    ]

    data_smoke_drink = [
        param_counter['Smokes'],
        param_counter['Drinks'],
        param_counter['Smokes and Drinks']      
    ]

    data_self_med = [
        param_counter['Med_No'],
        param_counter['Med_Always']        
    ]

    data = { 

        'common_disease': {
            'label': sickness,
            'data': data_sickness    
        },

        'sport_choices':{
            'label': sport_choices,
            'data': data_sport_choices
        },

        'drink_choices':{
            'label': smoke_drink_option,
            'data': data_smoke_drink
        },

        'med_choices':{
            'label': self_med,
            'data': data_self_med
        },
    }
    
    import pprint
    pprint.pprint(data)
    
    return render(request, 'patient_dashboard.html', {"data":data})
