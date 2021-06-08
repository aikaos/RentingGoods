from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Owners', views.OwnerView)
router.register('Goods', views.GoodsView)
router.register('Operation', views.OperationView)
router.register('Deposit', views.DepositView)
router.register('Category', views.CategoryView)
router.register('Branch', views.BranchView)

urlpatterns = [
    path('', include(router.urls)),
    path('goods-details/<int:pk>/', views.DetailGoods.as_view()),

]