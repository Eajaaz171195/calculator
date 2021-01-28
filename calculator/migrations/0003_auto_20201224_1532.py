# Generated by Django 3.1.1 on 2020-12-24 10:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20201224_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numeric_fields',
            name='inp_number1',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='numeric_fields',
            name='inp_number2',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='numeric_fields',
            name='result',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
    ]