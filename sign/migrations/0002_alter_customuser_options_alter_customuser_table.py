# Generated by Django 4.2.9 on 2024-01-26 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='sign_customuser',
        ),
    ]