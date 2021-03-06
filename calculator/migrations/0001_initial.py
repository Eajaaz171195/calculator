# Generated by Django 3.1.1 on 2020-12-24 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numeric_fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inp_number1', models.IntegerField(max_length=10)),
                ('inp_number2', models.IntegerField(max_length=10)),
                ('result', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_text', models.CharField(max_length=1)),
                ('numbers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.numeric_fields')),
            ],
        ),
    ]
