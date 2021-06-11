from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from datetime import datetime

# Create your models here.

class Deposit(models.Model):
    deposit_cost = models.FloatField(verbose_name='Залог', default=0)

    def __str__(self):
        return f"{self.deposit_cost}"


class Category(models.Model):
    name = models.CharField('Тип', max_length=100)
    active = models.BooleanField(verbose_name='Активный',default=True)

    def __str__(self):
        return f"{self.name}"


class TheCost(models.Model):
    price = models.FloatField(verbose_name='Цена')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')
    end_date = models.DateTimeField(default=datetime(2999, 12, 31, 00, 00, 00), null=True)
    good = models.ForeignKey('Goods', on_delete=models.DO_NOTHING, verbose_name='Цена проката')

    def __str__(self):
        return f"{self.price}"


class Owner(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    registration_date = models.DateTimeField(verbose_name='Дата регистрации',
                                             auto_now_add=True)
    phone_number = models.CharField('Телефонный номер', max_length=50)
    account = models.OneToOneField(User, models.CASCADE, null=True, related_name='account')

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}."


class PaymentAccount(models.Model):
    name = models.CharField('Счет оплаты', max_length=255)
    account_type = models.ForeignKey('AccountType', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.name}"


# class Account(models.Model):
#     login = models.CharField('Логин', max_length=50)
#     password = models.CharField('Пароль', max_length=50)
#     dealer = models.OneToOneField(Owner, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "login and Password"


class Goods(models.Model):
    name = models.CharField("Наименование товара", max_length=200)
    deposit = models.ForeignKey(Deposit, on_delete=models.DO_NOTHING, verbose_name='Залог', null=True)
    category_of_goods = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Тип', null=True)
    branch = models.ForeignKey('Branch', on_delete=models.DO_NOTHING, verbose_name='Арендатор', null=True)
    barcode = models.CharField('Баркод', max_length=50, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Operation(models.Model):
    start_date = models.DateTimeField(verbose_name='Дата получения')
    end_date = models.DateTimeField(verbose_name='Дата возврата')
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='Товар')
    total_price = models.FloatField()
    amount = models.IntegerField(verbose_name='Количество', null=True, blank=True)
    branch = models.ForeignKey('Branch', on_delete=models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, null=True)
    renter = models.ForeignKey('Renter', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f" Операция - {self.good}"


class Renter(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    passport_inn = models.CharField('Номер паспорта', max_length=20)
    phone_number = models.CharField('Телефонный номер', max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}."


class AccountType(models.Model):
    method = models.CharField('Оплата через:', max_length=50)
    def __str__(self):
        return f'{self.method}'


class Branch(models.Model):
    name = models.CharField('Наименование', max_length=100, null=True, blank=False)
    street = models.CharField('Улица', max_length=200)
    city = models.CharField(max_length=100)
    district = models.CharField('Район', max_length=50)
    dealer = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    house = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}, {self.street} {self.house}'


