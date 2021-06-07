from django.shortcuts import render
from .models import Owner, Goods, Operation
from .serializers import OwnerSerializer, GoodsSerializer, OperationSerializer
from rest_framework import viewsets
# Create your views here.


class OwnerView(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class GoodsView(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class OperationView(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
