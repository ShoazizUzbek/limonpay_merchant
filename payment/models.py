from django.contrib.auth.models import User
from django.db import models

from merchant.models import Merchant


class PaymentHistory(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming the user making the payment
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)