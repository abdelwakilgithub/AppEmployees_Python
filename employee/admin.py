from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


# Register your models here.

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_department']
    ordering = ['name']
    search_fields = ['name']


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['department', 'manager']
    list_display = ['id', 'first_name', 'last_name',  'email', 'fndepartment']
    list_editable = ['email']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
    list_filter = ['department']

    @admin.display(ordering='department')
    def fndepartment(self, employee):
        url = (
            reverse('admin:employee_employee_changelist')
            + '?'
            + urlencode({
                'id': str(employee.id)
            }))
        return format_html('<a href="{}">{}</a>', url, employee.department)

