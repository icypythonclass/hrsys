from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class EmployeesConfig(ModuleMixin, AppConfig):
    name = 'employees'
    icon = '<i class="material-icons">settings_applications</i>'
