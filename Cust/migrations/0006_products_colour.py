# Generated by Django 4.2.1 on 2023-06-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cust', '0005_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='colour',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]