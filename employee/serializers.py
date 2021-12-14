from decimal import Decimal

from django.db.models import fields
from employee.models import Employee, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'parent_department']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name']


class EmployeesSerializer(serializers.ModelSerializer):

    department = DepartmentSerializer()
    manager = ManagerSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'department',
                  'email', 'phone', 'birth_date', 'manager']


class AddEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'department',
                  'email', 'phone', 'birth_date', 'manager']
