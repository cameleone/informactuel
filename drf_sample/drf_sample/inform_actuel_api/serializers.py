from rest_framework import serializers

from inform_actuel.models import Acteur, Realisateur, Genre, Movie, Comment, Panier
from django.contrib.auth.models import User


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "description_gen", "id"
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "username"
        )


class ActeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acteur
        fields = (
            "id", "code_act", "nom_act", "prenom_act", "date_naissance_act",
            "gender_act"
        )


class RealisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realisateur
        fields = (
            "id", "code_real", "nom_real", "prenom_real", "date_naissance_real",
            "gender_real"
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id", "code_gen", "description_gen"
        )


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(required=False)
    acteurs = ActeurSerializer(many=True)
    realisateurs = RealisateurSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            "id", "type", "acteurs", "realisateurs", "genre", "photo", "code", "titre", "resume",
            "duree", "url_trailer", "date_sortie", "url_detail", "date_publication"
        )


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    # movie= MovieSerializer(required=False)
    class Meta:
        model = Comment
        fields = (
            "content", "movie", "author"
        )


class PanierSerializer(serializers.ModelSerializer):
    utilisateur = UserSerializer(required=False)

    # movie= MovieSerializer(required=False)
    class Meta:
        model = Panier
        fields = (
            "created_date", "movie", "utilisateur"
        )


class PanierListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(required=False)

    class Meta:
        model = Panier
        fields = (
            "created_date", "movie", "utilisateur"
        )
        # def get_validation_exclusions(self):
        #     # Need to exclude `user` since we'll add that later based off the request
        #     exclusions = super(CommentSerializer, self).get_validation_exclusions()
        #     return exclusions + ['author']
