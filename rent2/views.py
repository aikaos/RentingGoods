from django.shortcuts import render
from .models import Owner, Goods, Operation, Deposit, Category, Branch
from django.views.generic.list import ListView
# Create your views here.


class OwnerListView(ListView):
    model = Owner
    template_name = 'operations/operation.html'

def show_main(request):
    return render(request, 'main/main.html')

