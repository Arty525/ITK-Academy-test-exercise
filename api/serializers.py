from rest_framework import serializers

from api.models import Wallet
from api.validators import WalletCreateAmountValidator


class WalletUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
        validators = [
            WalletCreateAmountValidator(amount="amount"),
        ]
