from django.contrib import admin

from.models import Renter, Owner, Category, TheCost, Deposit, \
    Goods, RentOperation, Branch, Account, AccountType, PaymentAccounts
# Register your models here.

admin.site.register(Renter)
admin.site.register(Owner)
admin.site.register(Category)
admin.site.register(TheCost)
admin.site.register(Deposit)
admin.site.register(Goods)
admin.site.register(RentOperation)
admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(PaymentAccounts)