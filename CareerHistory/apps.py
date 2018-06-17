from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class CareerHistoryConfig(ModuleMixin, AppConfig):
    name = 'CareerHistory'
    verbose_name = '職務経歴'
    icon = '<i class="material-icons">settings_applications</i>'