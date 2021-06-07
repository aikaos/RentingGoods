from rest_framework import serializers
from .models import Owner, Goods, Operation, Deposit, Category, Branch


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class DepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'