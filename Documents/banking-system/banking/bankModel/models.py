from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=100, unique=True)
    swift_code = models.CharField(max_length=11, blank=True, null=True) 
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self) :
        return f"{self.bank_name}"
