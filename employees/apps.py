from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class EmployeesConfig(ModuleMixin, AppConfig):
    name = 'employees'
    verbose_name = '人事管理'
    icon = '<i class="material-icons">settings_applications</i>'
