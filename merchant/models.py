from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from merchant.constants import FieldTypeChoice


class MerchantCategory(models.Model):
    title = models.CharField(max_length=255, unique=True, )

    class Meta:
        verbose_name = 'Merchant Category'
        verbose_name_plural = 'Merchant Categories'
        db_table = 'merchant_category'

    def __str__(self):
        return f'{self.title}'


class Merchant(models.Model):
    category = models.ForeignKey(
        'merchant.MerchantCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='merchants',
    )
    title = models.CharField(max_length=255, )

    class Meta:
        verbose_name = 'Merchant'
        verbose_name_plural = 'Merchants'
        db_table = 'merchant'

    def __str__(self):
        return f'{self.title}'


class FieldModel(models.Model):
    title = models.CharField(max_length=255, )
    field_type = models.CharField(
        choices=FieldTypeChoice.choices,
        max_length=10,
    )

    def __str__(self):
        return f'{self.title} - {self.field_type}'


class DynamicMerchantField(models.Model):
    merchant = models.ForeignKey(
        Merchant,
        on_delete=models.CASCADE,
        related_name='fields',
    )
    field_type = models.ForeignKey(
        FieldModel,
        on_delete=models.CASCADE,
    )
    limit = models.Q(app_label = 'common')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to=limit
    )

    def __str__(self):
        return f'{self.field_type}'
