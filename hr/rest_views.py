from rest_framework import serializers
from .models import Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'fullname', 'title', 'salary')


def employees_client(request):
    return render(request, "rest_client.html")


@api_view(['GET', 'POST'])
def employees_get_post(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    else:  # POST
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Insert
            return Response(serializer.data)
        else:  # Error
            return Response(serializer.errors, status=400)  # Bad request


@api_view(['DELETE', 'GET'])
def process_one_employee(request, id):
    try:
        emp = Employee.objects.get(id=id)
    except:
        return Response(status=404)

    if request.method == "GET":
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)
    else: # DELETE
        emp.delete()
        return Response(status=204)  # No content
