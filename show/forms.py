from django import forms
from .models import Employee,EmployeeProject,Department,Project

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class EmployeeProjectForm(forms.ModelForm):
    class Meta:
        model = EmployeeProject
        fields = "__all__"

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"