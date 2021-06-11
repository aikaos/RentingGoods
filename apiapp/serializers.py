from django.contrib.auth.models import User
from rest_framework import serializers
from rent2.models import Owner, Goods, Operation, Deposit, Category, Branch, \
    Renter


class OwnerSerializer(serializers.ModelSerializer):
    account = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Owner
        fields = '__all__'



class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    # category_of_goods = serializers.SlugRelatedField('name', read_only=True)
    # deposit = serializers.SlugRelatedField('deposit_cost', read_only=True)
    # branch = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Goods
        fields = '__all__'


class DepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    good = serializers.SlugRelatedField('name', read_only=True)
    owner = serializers.SlugRelatedField('last_name', read_only=True)
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

class RenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Renter
        fields = '__all__'


# class AccountSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         fields = '__all__'