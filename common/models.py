from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255, )

    def __str__(self):
        return f'{self.name}'


class District(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='districts',
    )
    name = models.CharField(max_length=255, )

    def __str__(self):
        return f'{self.name}'

class ElectricalNetworkDistrict(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='ENDs',
    )
    name = models.CharField(max_length=255, )

    def __str__(self):
        return f'{self.name}'

class PaymentType(models.Model):
    title = models.CharField(max_length=255, )
    value = models.CharField(max_length=155, )

    def __str__(self):
        return f'{self.title}'