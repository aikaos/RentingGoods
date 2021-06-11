from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Operation)
admin.site.register(Owner)
admin.site.register(Deposit)
admin.site.register(TheCost)
admin.site.register(Category)
admin.site.register(PaymentAccount)
# admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(Goods)
admin.site.register(Renter)
admin.site.register(Branch)