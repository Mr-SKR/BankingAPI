from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    CreateBankView, DetailsBankView, CreateBranchView, DetailsBranchView,
    GetBankView
)

urlpatterns = {
    url(r'^banks(?P<pk>[0-9]+)/$',
        DetailsBankView.as_view(), name="details"),
    path('', GetBankView.as_view(), name="get"),
    url(r'^branch/$', CreateBranchView.as_view(), name="create"),
    url(r'^branch/(?P<pk>[A-Z0-9]{11})/$',
        DetailsBranchView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
