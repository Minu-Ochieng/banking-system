from django.db import models

# Create your models here.
class Bank(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    swift_code = models.CharField(max_length=11, blank=True, null=True)  # For international identification
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self) :
        return f"{self.name}"
