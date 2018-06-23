from material.frontend.views import ModelViewSet, CreateModelView
from material import Layout, Row
from django.views.generic import CreateView
from material.frontend.views import ModelViewSet

from . import models


class EmployeeCreateView(CreateModelView):
    layout = Layout(
        Row('birth_date'),
        Row('last_name', 'first_name', 'gender',),
        Row('hire_date'),
    )

    def has_add_permission(self, request):
        return True


class EmployeeViewSet(ModelViewSet):
    model = models.Employee
    create_view_class = EmployeeCreateView



class AttendanceViewSet(ModelViewSet):
    model = models.Attendance


class TechnologyViewSet(ModelViewSet):
    model = models.Technology


class CareerViewSet(ModelViewSet):
    model = models.CareerHistory
