from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee_name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.project_name


class EmployeeProject(models.Model):
    emp_proj_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)   
    project = models.ForeignKey(Project, on_delete=models.CASCADE)     
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee} - {self.project} ({self.role})"
