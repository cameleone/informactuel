"""drf_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# from django.conf.urls import include, url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

# from django.contrib import admin
# from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

#
# router = DefaultRouter()
# router.register(prefix='chains', viewset=ChainViewSet)
# router.register(prefix='stores', viewset=StoreViewSet)
# router.register(prefix='employees', viewset=EmployeeViewSet)
#
#
# urlpatterns = router.urls
from inform_actuel.views import LoginView,LogoutView



urlpatterns = [

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include("drf_sample.retail.urls", namespace="chains-api")),
    url(r'^api/inform/', include("drf_sample.inform_actuel_api.urls", namespace="movies-api")),
    url(r'^home/', include("client.urls", namespace="home")),
    url(r'^$', LoginView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^homes/', include("inform_actuel.urls", namespace="home_inf")),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
