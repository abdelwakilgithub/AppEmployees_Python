from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Department, Employee
from .serializers import AddEmployeeSerializer, DepartmentSerializer, EmployeesSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeesSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return AddEmployeeSerializer
        return EmployeesSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


@api_view(['GET', 'POST'])
def employees_list(request):
    if request.method == 'GET':
        queryset = Employee.objects.select_related('department').all()
        serializer = EmployeesSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def employee_detail(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'GET':
        serializer = EmployeesSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
