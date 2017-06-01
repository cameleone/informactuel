from django.contrib import admin

from drf_sample.retail.models import Chain
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_sortie')
    search_fields = ('titre','date_sortie')
    list_filter = ('date_sortie',)

admin.site.register(Movie,MovieAdmin)
admin.site.register(Acteur)
admin.site.register(Realisateur)
admin.site.register(Genre)
admin.site.register(Chain)
admin.site.register(Profil)
admin.site.register(Comment)
admin.site.register(Panier)
