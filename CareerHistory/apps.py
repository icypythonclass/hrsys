from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class CareerhistoryConfig(ModuleMixin, AppConfig):
    name = 'CareerHistory'
    icon = '<i class="material-icons">settings_applications</i>'
