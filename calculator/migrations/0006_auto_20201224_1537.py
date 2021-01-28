# Generated by Django 3.1.1 on 2020-12-24 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_auto_20201224_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numeric_fields',
            name='inp_number2',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
