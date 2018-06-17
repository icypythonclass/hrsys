from django.conf.urls import url, include
from django.views import generic

from . import views


urlpatterns = [
    url('^$', generic.RedirectView.as_view(url='./case/'), name="index"),
    url('^case/', include(views.CaseViewSet().urls)),
]