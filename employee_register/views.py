from .forms import EmployeeForm
from django.shortcuts import render

# Create your views here.

def employee_list(request):
    return render(request, 'employee_register/employee_list.html')


def employee_form(request):
    form = EmployeeForm
    return render(request, 'employee_register/employee_form.html', {'form': form})


def employee_delete(request):
    return