from django.contrib import admin
from employees.models import Employee
# Register your models here.




class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','firstName', 'lastName', 'salary', 'email']

admin.site.register(Employee, EmployeeAdmin)