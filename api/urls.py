from django.urls import path
from api.views import (
    WalletListAPIView,
    WalletDetailAPIView,
    WalletUpdateAPIView,
    WalletDeleteAPIView,
    WalletCreateAPIView,
)

app_name = "api"

urlpatterns = [
    path("v1/wallets/", WalletListAPIView.as_view(), name="list"),
    path("v1/wallets/<int:pk>/", WalletDetailAPIView.as_view(), name="detail"),
    path(
        "v1/wallets/<int:pk>/operation/", WalletUpdateAPIView.as_view(), name="update"
    ),
    path("v1/wallets/<int:pk>/delete/", WalletDeleteAPIView.as_view(), name="delete"),
    path("v1/wallets/create/", WalletCreateAPIView.as_view(), name="create"),
]
