from rest_framework import status
from rest_framework.response import Response

from .models import Wallet
from .serializers import WalletUpdateSerializer


def change_wallet_amount(wallet: Wallet, amount: int, operation_type: str) -> Response:
    if amount <= 0:
        return Response(
            {"error": "Amount cannot be less than zero"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if operation_type.upper() == "DEPOSIT":
        amount = amount + wallet.amount
    elif operation_type.upper() == "WITHDRAW":
        if amount > wallet.amount:
            return Response(
                {"error": "There are insufficient funds in the wallet"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        amount = wallet.amount - amount
    else:
        return Response(
            {"error": "Invalid operation_type"}, status=status.HTTP_400_BAD_REQUEST
        )
    serializer = WalletUpdateSerializer(wallet, data={"amount": amount})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
