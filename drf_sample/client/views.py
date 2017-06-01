from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from drf_sample.retail.models import Chain

#
# class LoginView(TemplateView):
#     template_name = 'front/index.html'
#
#     def post(self, request, **kwargs):
#         username = request.POST.get('username', False)
#         password = request.POST.get('password', False)
#         user = authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
#
#         return render(request, self.template_name)
#
#
# class LogoutView(TemplateView):
#     template_name = 'front/index.html'
#
#     def get(self, request, **kwargs):
#         logout(request)
#
#         return render(request, self.template_name)


def home(request):
    return render(request, 'home.html', {'STATIC_URL': settings.STATIC_URL})


def detail(request, chain_id):
    chain = get_object_or_404(Chain, pk=chain_id)
    return render(request, 'detail.html', {'chain': chain})
