# Generated by Django 4.2.1 on 2023-06-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='image',
            field=models.ImageField(default=None, upload_to='userimg'),
        ),
    ]
