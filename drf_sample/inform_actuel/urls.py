from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    # url(r'^movie/detail/(?P<movie_id>[0-9]+)/$', views.details, name="movie_detail"),
    url(r'^$', login_required(TemplateView.as_view(template_name='base/base.html'))),
    # url(r'^chain/detail/(?P<chain_id>[0-9]+)/$', views.detail, name="chain_detail"),
    # url(r'^$', login_required(TemplateView.as_view(template_name='backoffice/home.html'))),


]
