from django.conf.urls import url, include

from .views import (
    MovieAPIView,
    MovieDetailAPIView,
    CommentAPIView,
    GenreAPIView,
    PanierAPIView,
    PanierListAPIView,
CurrentUserAPIView

)


urlpatterns = [
    url(r'^movies/$', MovieAPIView.as_view(), name="movie_list"),
    url(r'^movies/(?P<pk>\d+)$', MovieDetailAPIView.as_view(), name='movie-detail'),
    url(r'^comments/$', CommentAPIView.as_view(), name ='comment_list'),
    url(r'^paniers/$', PanierAPIView.as_view(), name ='panier_list'),
    url(r'^paniersList/$', PanierListAPIView.as_view(), name ='paniers_list'),
    url(r'^genres/$', GenreAPIView.as_view(), name="genre_list"),
    url(r'^currentUser/$', CurrentUserAPIView.as_view(), name ='user_current')
    # url(r'^(?P<pk>[0-9]+)/acteurs$', MovieActeurList.as_view(), name='movieacteur-list')
]

# csrf_exempt(