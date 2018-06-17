from material.frontend.views import ModelViewSet

from . import models


class CareerViewSet(ModelViewSet):
   model = models.CareerHistory
