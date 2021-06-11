from rest_framework.generics import get_object_or_404

from rent2.models import Owner, Goods, Operation, Deposit, Category, Branch, Renter
from .serializers import OwnerSerializer, GoodsSerializer, OperationSerializer, DepositSerializer, CategorySerializer, \
    BranchSerializer, RenterSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
# Create your views here.

class RenterView(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class DetailGoods(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class OwnerView(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class GoodsView(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class OperationView(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer


class DepositView(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
