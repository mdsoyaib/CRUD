from .forms import EmployeeForm
from django.shortcuts import redirect, render

# Create your views here.

def employee_list(request):
    return render(request, 'employee_register/employee_list.html')


def employee_form(request):
    if request.method == "GET":
        form = EmployeeForm
        return render(request, 'employee_register/employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("employee_list")


def employee_delete(request):
    return