from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.view_employee, name='view_employee'),
    path('department/', views.view_department, name='view_department'),
    path('project/', views.view_project, name='view_project'),
    path('employeeproject/', views.view_employeeproject, name='view_employeeproject'),

    path('employee/create/', views.employee_create, name='employee_create'),
    path('employee/<int:employee_id>/edit/', views.employee_edit, name='employee_edit'),
    path('employee/<int:employee_id>/delete/', views.employee_delete, name='employee_delete'),

    path('department/create/', views.department_create, name='department_create'),
    path('department/<int:department_id>/edit/', views.department_edit, name='department_edit'),
    path('department/<int:department_id>/delete/', views.department_delete, name='department_delete'),

    path('project/create/', views.project_create, name='project_create'),
    path('project/<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('project/<int:project_id>/delete/', views.project_delete, name='project_delete'),

    path('employee_project/create/', views.empproject_create, name='employee_project_create'),
    path('employee_project/<int:emp_project_id>/edit/', views.empproject_edit, name='employee_project_edit'),
    path('employee_project/<int:emp_project_id>/delete/', views.empproject_delete, name='employee_project_delete'),
]
