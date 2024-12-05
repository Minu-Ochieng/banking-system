from django.db import models

from bankModel.models import Bank
from client.models import Client

# Create your models here.

class BankAccount(models.Model):
    bank_account_id = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=30, unique=True)
    account_type = models.CharField(max_length=20, choices=[("Savings", "Savings"), ("Checking", "Checking"), ("Business", "Business")])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="bank_accounts")
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, blank=True, null=True, related_name="accounts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_number}"
