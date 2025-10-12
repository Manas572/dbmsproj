from django.contrib import admin
from .models import Employee
from .models import Project
from .models import Department
from .models import EmployeeProject
# Register your models here.


admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(EmployeeProject)
