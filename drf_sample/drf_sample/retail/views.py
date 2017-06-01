from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from django.http import HttpResponse, Http404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Chain, Store, Employee
from .serializers import ChainSerializer, StoreSerializer, EmployeeSerializer


class ChainAPIView(APIView):
    def get(self, request, format=None):
        chains = Chain.objects.all()
        serializer = ChainSerializer(chains, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def get_object(pk):
#     try:
#         return Chain.objects.get(pk=pk)
#     except Chain.DoesNotExist:
#         raise Http404


class ChainDetailAPIView(APIView):
    def get(self, request, pk, format=None):
        chain = Chain.objects.get(pk=pk)
        serializer = ChainSerializer(chain)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        chain = Chain.objects.get(pk=pk)
        serializer = ChainSerializer(chain, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        chain = Chain.objects.get(id=pk)
        chain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoreAPIView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
