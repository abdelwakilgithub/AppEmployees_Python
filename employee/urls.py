from django.urls import path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)


urlpatterns = router.urls
#  [
#     path('employees/', views.employees_list),
#     path('employee/<id>/', views.employee_detail),
# ]
