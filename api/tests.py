from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from api.models import Wallet


class WalletsAPIViewTestCase(TestCase):
    def setUp(self):
        self.test_wallet = Wallet.objects.create(amount=10000)
        self.test_wallet.save()

        self.second_test_wallet = Wallet.objects.create(amount=500)
        self.second_test_wallet.save()

        self.client = APIClient()

    def test_get_all_wallets(self):
        response = self.client.get("/api/v1/wallets/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_one_wallet(self):
        response = self.client.get(
            f"/api/v1/wallets/{str(self.second_test_wallet.pk)}/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["amount"], 500)


class WalletUpdateAPIViewTestCase(TestCase):
    def setUp(self):
        self.test_wallet = Wallet.objects.create(amount=900)
        self.test_wallet.save()

        self.client = APIClient()

    def test_operation_deposit(self):
        current_amount = self.test_wallet.amount
        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "DEPOSIT", "amount": 100},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Wallet.objects.get(pk=self.test_wallet.pk).amount, current_amount + 100
        )

    def test_operation_withdraw(self):
        current_amount = self.test_wallet.amount
        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "WITHDRAW", "amount": 100},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Wallet.objects.get(pk=self.test_wallet.pk).amount, current_amount - 100
        )

    def test_operation_errors(self):
        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "DEPOSIT", "amount": -100},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "WITHDRAW", "amount": -100},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "DEPOSIT", "amount": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "WITHDRAW", "amount": 0},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(
            f"/api/v1/wallets/{self.test_wallet.pk}/operation/",
            data={"operation_type": "OPERATION", "amount": 100},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class WalletDeleteAPIViewTestCase(TestCase):
    def setUp(self):
        self.test_wallet = Wallet.objects.create(amount=10000)
        self.test_wallet.save()

        self.client = APIClient()

    def test_wallet_delete(self):
        response = self.client.delete(f"/api/v1/wallets/{self.test_wallet.pk}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class WalletCreateAPIViewTestCase(TestCase):
    def test_create_wallet(self):
        response = self.client.post("/api/v1/wallets/create/", data={"amount": 0})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/api/v1/wallets/create/", data={"amount": 100})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post("/api/v1/wallets/create/", data={"amount": -100})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get("/api/v1/wallets/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
