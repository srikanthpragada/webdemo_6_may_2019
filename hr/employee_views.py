from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import datetime
from .forms import EmployeeForm
from .models import Employee


def list_employees(request):
    emps = Employee.objects.all()
    return render(request, 'list_employees.html', {"emps": emps})


def add_employee(request):
    message = ""
    if request.method == "GET":
        f = EmployeeForm()
    else:  # post
        f = EmployeeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/hr/listemployees")
        else:
            message = "Sorry! Invalid data. Please try again!"

    return render(request, 'add_employee.html', {"form": f, "message": message})


def delete_employee(request, id):
    message = ""
    try:
        emp = Employee.objects.get(id=id)
        emp.delete()
        message = f"Employee [{emp.fullname}] was deleted!"
    except:
        message = f"Sorry! Employee Id [{id}] not found!"

    return render(request, 'delete_employee.html', {"message": message})


def edit_employee(request, id):
    if request.method == "GET":
        try:
            emp = Employee.objects.get(id=id)
            f = EmployeeForm(instance=emp)
            return render(request, 'edit_employee.html',
                          {'form': f})
        except:
            return render(request, 'edit_employee.html',
                          {'message': f"Employee With ID {id} Not Found!"})
    else:  # Post
        # Update Employee
        emp = Employee.objects.get(id=id)
        f = EmployeeForm(request.POST, instance=emp)
        if f.is_valid():
            f.save()  # Updation
            return redirect("/hr/listemployees")
        else:
            return render(request, 'edit_employee.html',
                          {'form': f,
                           'message': 'Invalid Data. Please correct and resubmit'})


def emp_count(request):
    return HttpResponse(len(Employee.objects.all()))


def search_employees_form(request):
    if 'pattern'  in request.COOKIES:
        pattern = request.COOKIES['pattern']
    else:
        pattern = ''

    return render(request, 'search_employees.html',
                  {'pattern' : pattern })

# Returns array of JSON objects
def search_employees(request):
    name = request.GET["name"]
    emps = Employee.objects.filter(fullname__contains=name).values()
    emplist = list(emps)
    response = JsonResponse(emplist,safe=False)
    response.set_cookie("pattern", name,
       expires=datetime.datetime.now() + datetime.timedelta(days=10))
    return response




