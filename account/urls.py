from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard', Dashboard, name='dashboard'),
    path('departmentList', DepartmentList, name='departmentList'),
    path('departmentAdd', DepartmentAdd, name='departmentAdd'),
    path('departmentDelete/<int:id>',DeptDelete,name='departmentDelete'),
    path('register/<int:role>', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    ]