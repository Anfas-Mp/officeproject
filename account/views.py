from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from account.models import *
from django.contrib import messages


def Dashboard(request):
    return render(request, 'account/base.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def register_view(request, role):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = role

        if not username or not email or not password1 or not password2:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('register', role)

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register', role)

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email id is already exist.')
            return redirect('register', role)

        if password1 == password2:

            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password2,
                role=role
            )



    return render(request, 'account/register.html')


# def Dashboard(request):
#     user_count = CustomUser.objects.count()
#     return render(request, 'dashboard.html', {user_count: "user_count"})


def logout_view(request):
    logout(request)
    return redirect('login')


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'account/user_list.html', {'users': users})


def user_status_change(request, id):
    user = CustomUser.objects.get(id=id)
    user.is_active = not user.is_active
    user.save()
    return redirect('user_list')


def user_delete(request, id):
    user = CustomUser.objects.get(id=id)
    if user:
        user.delete()
    else :
        messages.error(request, 'user not exist')
    return redirect('user_list')

def DepartmentList(request):
    dept = Department.objects.all()
    context = {
        'department' : dept,
    }
    return render(request, 'account/departmentList.html',context)

def DepartmentAdd(request):

    if request.method == 'POST':
        deptName = request.POST.get('dept_name')
        Department.objects.create(
            DeptName=deptName,
        )

    return render(request, 'account/departmentAdd.html')

def DeptDelete(request,id):
    dept=Department.objects.get(id=id)
    if request.method =="POST":
        dept.delete()
        return redirect('Departmentlist')
    context ={}
    return render(request,'user_delete.html',context)
