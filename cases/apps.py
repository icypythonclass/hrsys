from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class CasesConfig(ModuleMixin, AppConfig):
    name = 'cases'
    verbose_name = '案件'
    icon = '<i class="material-icons">assignment</i>'
