# Generated by Django 4.1 on 2022-08-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myShop', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='ordered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
