
from . import views, job_views
from django.urls import path

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.goodbye),
    path('countries/', views.list_countries),
    path('addjob/', job_views.add_job),
    path('addjob2/', job_views.add_job_with_form),
    path('listjobs/', job_views.list_jobs),
]
