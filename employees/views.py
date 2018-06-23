from material.frontend.views import ModelViewSet, CreateModelView, UpdateModelView, DetailModelView
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


class CareerCreateView(CreateModelView):
    layout = Layout(
        Row('employee','company'),
        Row('start_date', 'end_date', ),
        Row('role', 'department'),
        Row('contribution'),
    )

    def has_add_permission(self, request):
        return True


class CareerDetailView(DetailModelView):
    layout = Layout(
        Row('employee', 'company'),
        Row('start_date', 'end_date', ),
        Row('role', 'department'),
        Row('contribution'),
    )


class CareerUpdateView(UpdateModelView):
    layout = Layout(
        Row('employee', 'company'),
        Row('start_date', 'end_date', ),
        Row('role', 'department'),
        Row('contribution'),
    )


class EmployeeViewSet(ModelViewSet):
    model = models.Employee
    create_view_class = EmployeeCreateView



class AttendanceViewSet(ModelViewSet):
    model = models.Attendance


class TechnologyViewSet(ModelViewSet):
    model = models.Technology


class CareerViewSet(ModelViewSet):
    model = models.CareerHistory
    create_view_class = CareerCreateView
    detail_view_class = CareerDetailView
    update_view_class = CareerUpdateView

