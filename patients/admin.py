from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from patients.models import User, Appointment, PatientsRecords


class AccountAdmin(UserAdmin):
    list_display = ('id','email', 'username', 'full_name', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()
    
admin.site.register(User, AccountAdmin)
admin.site.register(Appointment)
admin.site.register(PatientsRecords)

