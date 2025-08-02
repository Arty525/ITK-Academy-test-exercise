from django.db import models

# Create your models here.
class Wallet(models.Model):
    amount = models.IntegerField(verbose_name='Баланс')

    def __str__(self):
        return str(f'{self.pk} - {self.amount}')

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'
        ordering = ['amount']