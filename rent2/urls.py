from django.urls import path
from rent2.views import OwnerListView

from .views import show_main


urlpatterns = [
    path('', show_main, name='main'),
    path('owners-list/', OwnerListView.as_view(), name='opview'),
]