# Generated by Django 4.0.2 on 2022-02-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
