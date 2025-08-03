from rest_framework import generics
from api.models import Wallet
from api.serializers import WalletUpdateSerializer, WalletSerializer
from .services import change_wallet_amount


class WalletListAPIView(generics.ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDetailAPIView(generics.RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletCreateAPIView(generics.CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletUpdateAPIView(generics.UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletUpdateSerializer

    def post(self, request, pk):
        wallet = self.get_object()
        amount = int(request.data["amount"])
        operation_type = request.data["operation_type"]
        return change_wallet_amount(wallet, amount, operation_type)


class WalletDeleteAPIView(generics.DestroyAPIView):
    queryset = Wallet.objects.all()
