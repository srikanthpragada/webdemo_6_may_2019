
from . import views, job_views, employee_views

from django.urls import path

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.goodbye),
    path('countries/', views.list_countries),
    path('addjob/', job_views.add_job),
    path('addjob2/', job_views.add_job_with_form),
    path('listjobs/', job_views.list_jobs),
    path('editemployee/<int:id>', employee_views.edit_employee),
    path('listemployees/', employee_views.list_employees),
    path('addemployee/', employee_views.add_employee),
    path('deleteemployee/<int:id>', employee_views.delete_employee),
    path('searchform/', employee_views.search_employees_form),
    path('search/', employee_views.search_employees),
    path('ajaxdemo/', views.ajax_demo),
    path('empcount/', employee_views.emp_count),
]

