# Generated by Django 4.2.16 on 2024-10-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0002_dynamicmerchantfield_char_field_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynamicmerchantfield',
            name='field_name',
        ),
    ]