from material.frontend.views import ModelViewSet

from . import models


class EmployeeViewSet(ModelViewSet):
   model = models.Employee
