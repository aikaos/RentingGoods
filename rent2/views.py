from django.shortcuts import render
from .models import Owner, Goods, Operation, Deposit, Category, Branch
from django.views.generic.list import ListView
# Create your views here.


class OperationListView(ListView):
    model = Owner
    template_name = 'operations/operation.html'


