from django.shortcuts import render
from employees.models import Employee

def employee_info(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
        }
    return render (request, 'index.html', context)

