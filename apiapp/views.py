from rent2.models import Owner, Goods, Operation, Deposit, Category, Branch
from .serializers import OwnerSerializer, GoodsSerializer, OperationSerializer, DepositSerializer, CategorySerializer, \
    BranchSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
# Create your views here.


class DetailGoods(generics.RetrieveAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


class OwnerView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
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
