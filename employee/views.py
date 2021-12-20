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
