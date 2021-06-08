from django.urls import path
from rent2.views import OperationListView


urlpatterns = [
    path('', OperationListView.as_view(), name='opview')
]