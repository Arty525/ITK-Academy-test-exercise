from rest_framework import status, generics
from rest_framework.response import Response
from api.models import Wallet
from api.serializers import WalletUpdateSerializer, WalletSerializer


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
        if request.data['amount'] <= 0:
            return Response({'error': 'Amount cannot be less than zero'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['operation_type'] == 'DEPOSIT':
            request.data['amount'] = request.data['amount'] + wallet.amount
        elif request.data['operation_type'] == 'WITHDRAW':
            if request.data['amount'] > wallet.amount:
                return Response({'error': 'There are insufficient funds in the wallet'},
                                status=status.HTTP_400_BAD_REQUEST)
            request.data['amount'] = wallet.amount - request.data['amount']
        else:
            return Response({'error': 'Invalid operation_type'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = WalletUpdateSerializer(wallet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WalletDeleteAPIView(generics.DestroyAPIView):
    queryset = Wallet.objects.all()
