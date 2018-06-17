from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class CasesConfig(ModuleMixin, AppConfig):
    name = 'cases'
    icon = '<i class="material-icons">settings_applications</i>'
