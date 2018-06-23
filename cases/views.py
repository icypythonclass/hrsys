from material.frontend.views import ModelViewSet, CreateModelView
from material import Layout, Row

from . import models


class CaseCreateView(CreateModelView):
    layout = Layout(
        Row('case_name', 'case_place', 'case_belongings'),
        Row('case_start_time', 'case_end_time'),
        Row('case_industry', 'case_language', 'case_price'),
        Row('case_remark'),
    )

    def has_add_permission(self, request):
        return True


class CaseViewSet(ModelViewSet):
    model = models.Case
    create_view_class = CaseCreateView
