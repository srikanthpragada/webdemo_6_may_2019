
from . import views, job_views, employee_views, class_views, rest_views

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
    path('plist/', views.add_passenger),
    path('delpass/', views.delete_passenger),
    # class based views
    path('about/', class_views.AboutView.as_view()),
    path('wish/', class_views.WishView.as_view()),
    path('employees/', class_views.ListEmployeesView.as_view()),

    path('rest/employees/', rest_views.employees_get_post),
    path('rest/employees/<int:id>', rest_views.process_one_employee),
    path('rest/client/', rest_views.employees_client),
]

