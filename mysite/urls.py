from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_list,name='site_emplist'),
    path('add/',views.add_employees,name='site_register'),
    path('update',views.update_employees,name='site_update')
]