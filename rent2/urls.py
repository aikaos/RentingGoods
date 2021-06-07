from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Owners', views.OwnerView)
router.register('Goods', views.GoodsView)
router.register('Operation', views.OperationView)

urlpatterns = [
    path('', include(router.urls))
]