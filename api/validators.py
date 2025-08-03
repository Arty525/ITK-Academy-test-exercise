from rest_framework.exceptions import ValidationError


class WalletCreateAmountValidator:
    """
    Проверяет, чтобы сумма на балансе при создании счета была не ниже 0
    """

    def __init__(self, amount):
        self.amount = amount

    def __call__(self, fields):
        amount = fields.get("amount")
        if amount is not None:
            if amount < 0:
                raise ValidationError("Сумма должна быть не ниже 0")
