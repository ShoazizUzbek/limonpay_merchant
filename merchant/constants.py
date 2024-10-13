from django.db import models


class FieldTypeChoice(models.TextChoices):
    STRING = ('STRING', 'String')
    INTEGER = ('INTEGER', 'Integer')
    FOREIGNKEY = ('FOREIGNKEY', 'Foreignkey')