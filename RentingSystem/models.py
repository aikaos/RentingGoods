from django.db import models

from datetime import datetime
# Create your models here.


class Renter(models.Model):
    first_name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Surname', max_length=100)
    passport_inn = models.CharField('Passport number', max_length=20)
    phone_num = models.CharField('Phone number',max_length=50)


class Owner(models.Model):
    first_name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Surname', max_length=50)
    phone_number = models.CharField('Phone', max_length=50)
    registration_date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.DO_NOTHING)
    name = models.CharField('Name of category', max_length=100)
    active = models.BooleanField('Active', default=True)


class TheCost(models.Model):
    price = models.FloatField(verbose_name='Price')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(year=2999, month=12, day=31, hour=12, minute=12))
    goods = models.ForeignKey('Goods', on_delete=models.DO_NOTHING)


class Deposit(models.Model):
    deposit_cost = models.FloatField(default=0, verbose_name='Deposit cost')


class Goods(models.Model):
    name = models.CharField('Name of goods', max_length=50)
    active = models.BooleanField('Active', default=True)
    barcode = models.CharField('Barcode', max_length=50)
    category_of_goods = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Category of Goods')
    deposit = models.ForeignKey(Deposit, on_delete=models.DO_NOTHING, verbose_name='Price')
    branch = models.ForeignKey('Branch', on_delete=models.DO_NOTHING, verbose_name='Owner')


class RentOperation(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    amount = models.IntegerField(verbose_name='Quantity')
    total_price = models.FloatField(default=0.00)
    goods = models.ForeignKey(Goods, on_delete=models.DO_NOTHING)
    branch = models.ForeignKey('Branch', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    renter = models.ForeignKey(Renter, on_delete=models.DO_NOTHING)


class Branch(models.Model):
    city = models.CharField('City', max_length=100)
    street = models.CharField('Address', max_length=200)
    house = models.CharField('Phone number', max_length=50)
    district = models.CharField('District', max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)


class Account(models.Model):
    login = models.CharField('Login', max_length=50)
    password = models.CharField('Password', max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, related_name='owner')


class AccountType(models.Model):
    method = models.CharField('Method', max_length=50)


class PaymentAccounts(models.Model):
    name = models.CharField(max_length=100)
    account_type = models.ForeignKey(AccountType, on_delete=models.DO_NOTHING)