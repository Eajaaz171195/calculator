# Generated by Django 3.1.1 on 2020-12-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numeric_fields',
            name='inp_number1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='numeric_fields',
            name='inp_number2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='numeric_fields',
            name='result',
            field=models.IntegerField(),
        ),
    ]
