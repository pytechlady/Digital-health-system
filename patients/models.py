from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import validators
import uuid


"""Patients model"""
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70, unique=True, validators=[validators.EmailValidator()])
    username = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']
    
    objects = MyAccountManager()
    
    def __str__(self):
            return self.username
        
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
"""Patients model"""

"""Appointment Model"""
class Appointment(models.Model):
    SERVICE_CHOICES=(
        ('Optical Service', 'Optical Service'),
        ('Dental Service', 'Dental Service'),
        ('Pediatric Service', 'Pediatric Service'),
        ('Laboratory Service', 'Laboratory Service'),
    )
    TIME_CHOICES=(
        ('8AM TO 10AM','8AM TO 10AM'),
        ('10AM TO 12PM','10AM TO 12PM'),
        ('12PM TO 2PM','12PM TO 2PM'),
        ('2PM TO 4PM','2PM TO 4PM'),
        ('4PM TO 6PM','4PM TO 6PM'),
        ('6PM TO 8PM','6PM TO 8PM'),
        ('4PM TO 10PM','4PM TO 10PM'),
        ('10PM TO 12PM','10PM TO 12PM'),
         
    )
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    email= models.CharField(max_length=250)
    service= models.CharField(max_length=250, choices=SERVICE_CHOICES)
    time= models.CharField(max_length=250, choices=TIME_CHOICES)
    notes=models.TextField()
"""Appointment Model"""


# Patients Record Model
class PatientsRecords(models.Model):
    
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Binary", "Binary"),
    )
    DIAGNOSIS_CHOICES = (
        ("Malaria", "Malaria"),
        ("Fever", "Fever"),
        ("Cholera", "Cholera"),
        ("Cancer", "Cancer")
    )
    SPORT_EXCERCISE_CHOICES = (
        ("No", "No"),
        ("Sometimes", "Sometimes"),
        ("Always", "Always")
    )
    SMOKE_DRINK_CHOICES = (
        ("Smokes", "Smokes"),
        ("Drinks", "Drinks"),
        ("Smokes and Drinks", "Smokes and Drinks"),
        ("None", "None")
    )
    SELF_MEDICATION_CHOICE = (
        ("No", "No"),
        ("Always", "Always")
    )

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    address = models.TextField(max_length=255)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    occupation = models.CharField(max_length=200)
    allergies = models.CharField(max_length=255)
    recent_diagnosis = models.CharField(max_length=50, choices=DIAGNOSIS_CHOICES)
    sport_participation = models.CharField(max_length=50, choices=SPORT_EXCERCISE_CHOICES)
    sleep_routine = models.CharField(max_length=255)
    smoke_drink = models.CharField(max_length=50, choices=SMOKE_DRINK_CHOICES) 
    self_medication = models.CharField(max_length=255, choices=SELF_MEDICATION_CHOICE)
    

# Statistical analysis of Rate of self-medication
# Statistical analysis of the rate of smokers
# Statistical analysis of the rate of drinkers
# statistical analysis of the rate of common illness/disease
# Statistical analysis of the rate of patients performing regular physical activities

    
    
    
    
