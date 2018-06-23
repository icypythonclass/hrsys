from django.conf.urls import url, include
from django.views import generic

from . import views


urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./employee/'), name="index"),
    url('^employee/', include(views.EmployeeViewSet().urls)),
    url('^attendance/', include(views.AttendanceViewSet().urls)),
    url('^technology/', include(views.TechnologyViewSet().urls)),
    url('^career/', include(views.CareerViewSet().urls)),
    url('^salary/', include(views.SalaryViewSet().urls)),
]
