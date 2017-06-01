from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView

from .models import Movie



class LoginView(TemplateView):
    template_name = 'front/login.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'front/login.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)

# @permission_required('blog.commenter_article')
def home(request):
    return render(request, 'base/base.html', {'STATIC_URL': settings.STATIC_URL})


# def details(request, movie_id):
#     # movie = get_object_or_404(Movie, pk=movie_id)
#     movie = Movie.objects.get(pk=movie_id)
#     realisateurs = movie.realisateurs.all()
#     return render(request, 'details.html', {'movie': movie
#         , 'realisateurs': realisateurs,
#                                             })
