# Generated by Django 4.2.1 on 2023-06-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cust', '0004_remove_customers_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'women'), ('K', 'kids')], max_length=2),
        ),
    ]