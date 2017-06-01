from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import MovieSerializer, ActeurSerializer, CommentSerializer,GenreSerializer, PanierSerializer, PanierListSerializer, UserSerializer
from inform_actuel.models import Movie, Acteur, Comment, Genre, Panier
from django.contrib.auth.models import User



class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class CommentAuthorCanEditPermission(SafeMethodsOnlyPermission):
    """Allow everyone to list or view, but only the other can modify existing instances"""
    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            # Either a list or a create, so no author
            can_edit = True
        else:
            can_edit = request.user == obj.author
        return can_edit or super(CommentAuthorCanEditPermission, self).has_object_permission(request, view, obj)




class PostMixin(object):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        CommentAuthorCanEditPermission
    ]

    def perform_create(self, serializer):
        """Force author to the current user on save"""
        serializer.save(author=self.request.user)




class MovieAPIView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


class CommentAPIView(PostMixin,APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PanierListAPIView(APIView):
    def get(self, request, format=None):
        paniersList = Panier.objects.all()
        serializer = PanierListSerializer(paniersList, many= True)
        return  Response(serializer.data)


class PanierAPIView(APIView):
    def get(self, request, format=None):
        paniers = Panier.objects.all()
        serializer = PanierSerializer(paniers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PanierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(utilisateur=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CurrentUserAPIView(APIView):
    def get(self, request, format =None):
        user = request.user
        # currentUser = User.objects.get(id=user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ActeurAPIView(APIView):
    def get(self, request, format=None):
        acteurs = Acteur.objects.all()
        serializer = ActeurSerializer(acteurs, many=True)
        return Response(serializer.data)


class GenreAPIView(APIView):
    def get(self,request,format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MovieActeurList(generics.ListAPIView):
#     model = Acteur
#     queryset = Acteur.objects.all()
#     serializer_class = ActeurSerializer
#
#     def get_queryset(self):
#         queryset = super(MovieActeurList, self).get_queryset()
#         return queryset.filter(movie=self.kwargs.get('pk'))
