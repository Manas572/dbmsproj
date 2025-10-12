from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Project, EmployeeProject
from .forms import EmployeeForm, ProjectForm, EmployeeProjectForm, DepartmentForm
from django.db import connection

def view_employee(request):
    employees = Employee.objects.all()
    print(connection.queries)
    return render(request, 'view_employee.html', {"employees": employees})

def view_department(request):
    departments = Department.objects.all()
    print(connection.queries)
    return render(request, 'view_department.html', {"departments": departments})

def view_project(request):
    projects = Project.objects.all()
    print(connection.queries)
    return render(request, 'view_project.html', {"projects": projects})

def view_employeeproject(request):
    emp_projects = EmployeeProject.objects.all()
    print(connection.queries)
    return render(request, 'view_ep.html', {"emp_projects": emp_projects})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_employee')
    else:
        form = EmployeeForm()
    return render(request, 'form.html', {'form': form})

def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_department')
    else:
        form = DepartmentForm()
    return render(request, 'form.html', {'form': form})

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_project')
    else:
        form = ProjectForm()
    return render(request, 'form.html', {'form': form})

def empproject_create(request):
    if request.method == "POST":
        form = EmployeeProjectForm(request.POST)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_employeeproject')
    else:
        form = EmployeeProjectForm()
    return render(request, 'form.html', {'form': form})

def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_employeeproject')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'form.html', {'form': form})

def empproject_edit(request, emp_project_id):
    ep = get_object_or_404(EmployeeProject, pk=emp_project_id)
    if request.method == "POST":
        form = EmployeeProjectForm(request.POST, instance=ep)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_employeeproject')
    else:
        form = EmployeeProjectForm(instance=ep)
    return render(request, 'form.html', {'form': form})

def project_edit(request, project_id):
    pr = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=pr)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_project')
    else:
        form = ProjectForm(instance=pr)
    return render(request, 'form.html', {'form': form})

def department_edit(request, department_id):
    dt = get_object_or_404(Department, pk=department_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=dt)
        if form.is_valid():
            form.save()
            print(connection.queries)
            return redirect('view_department')
    else:
        form = DepartmentForm(instance=dt)
    return render(request, 'form.html', {'form': form})

def employee_delete(request, employee_id):
    obj = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        obj.delete()
        print(connection.queries)
        return redirect("view_employee")
    return render(request, "delete_confirm.html", {
        "object": obj,
        "list_url": "view_employee",
    })

def department_delete(request, department_id):
    obj = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        obj.delete()
        print(connection.queries)
        return redirect("view_department")
    return render(request, "delete_confirm.html", {
        "object": obj,
        "list_url": "view_department",
    })

def project_delete(request, project_id):
    obj = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        obj.delete()
        print(connection.queries)
        return redirect("view_project")
    return render(request, "delete_confirm.html", {
        "object": obj,
        "list_url": "view_project",
    })

def empproject_delete(request, emp_project_id):
    obj = get_object_or_404(EmployeeProject, pk=emp_project_id)
    if request.method == 'POST':
        obj.delete()
        print(connection.queries)
        return redirect("view_employeeproject")
    return render(request, "delete_confirm.html", {
        "object": obj,
        "list_url": "view_employeeproject",
    })
