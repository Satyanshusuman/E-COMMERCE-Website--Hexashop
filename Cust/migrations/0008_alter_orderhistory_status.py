# Generated by Django 4.2.1 on 2023-06-15 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cust', '0007_rename_shipping_price_products_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='status',
            field=models.CharField(choices=[('Accepted', 'accepted'), ('Packed', 'packed'), ('On The Way', 'on the way'), ('Deleivered', 'delivered'), ('Cancel', 'canceled')], default='pending', max_length=50),
        ),
    ]
