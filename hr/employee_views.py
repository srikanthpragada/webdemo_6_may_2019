from django.shortcuts import  render

def  list_employees(request):
    return render(request,'list_employees.html')


def  add_employee(request):
    return render(request,'add_employee.html')
