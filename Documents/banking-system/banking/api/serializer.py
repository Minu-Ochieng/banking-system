from client.models import Client
from rest_framework import serializers

from bankModel.models import Bank


from bankAccount.models import BankAccount



class ClientSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    user_name = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    kra_pin = serializers.EmailField(source='user.kra_pin')
    phone_number = serializers.CharField(source= 'user.phone_number')
    class Meta:
        model = Client
        fields = '__all__'

class MinimalClientSerializer(serializers.ModelSerializer):
    client_id = serializers.PrimaryKeyRelatedField(read_only=True)
    def get_kra_pin(self, obj):
        return obj.kra_pin
    class Meta:
        model = Client
        fields = '__all__'



class BankAccountSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField('user.account_number')
    account_type = serializers.CharField('user.account_type')
    bank = serializers.CharField('user.bank')
    client = serializers.CharField('user.client')
    class Meta:
        model = BankAccount
        fields = '__all__'



class BankModelSerializer(serializers.ModelSerializer):
    name  = serializers.CharField('user.name')
    swift_code = serializers.CharField('user.swift_code')
    branch_name = serializers.CharField('user.branch_name')
    class Meta:
        model = Bank
        fields = '__all__'


