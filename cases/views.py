from material.frontend.views import ModelViewSet

from . import models


class CaseViewSet(ModelViewSet):
    model = models.Case
