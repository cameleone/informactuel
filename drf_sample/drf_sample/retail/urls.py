from rest_framework import urlpatterns
from django.conf.urls import url

from .views import (
    ChainAPIView,
    StoreAPIView,
    ChainDetailAPIView,
)

urlpatterns = [
    url(r'^chains/$', ChainAPIView.as_view(), name="chain_list"),
    url(r'^chains/(?P<pk>[0-9]+)/$', ChainDetailAPIView.as_view(), name="chain_detail"),

    url(r'^stores/', StoreAPIView.as_view(), name="store_list"),
]