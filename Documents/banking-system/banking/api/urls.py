from django.urls import path
from .serializer import ClientSerializer
from . import views

from .views import ClientListView
from .views import BankAccountListView
from .views import BankListView



urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list_view'),
    path('bank-accounts/', BankAccountListView.as_view(), name='bank_account_list_view'),
    path('banks/', BankListView.as_view(), name='bank_list_view'),
]