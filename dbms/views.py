
from django.shortcuts import render

def fun1(request):
    tables = ['Department', 'Employee', 'Project', 'EmployeeProjec']
    return render(request, 'website/Home.html', {'tables': tables})