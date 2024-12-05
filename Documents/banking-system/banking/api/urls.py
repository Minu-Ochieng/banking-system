from django.urls import path
from .serializer import ClientSerializer
from . import views

from .views import ClientListView



urlpatterns = [

    path('clients/', ClientListView.as_view(), name='client_list_view'),
    
]