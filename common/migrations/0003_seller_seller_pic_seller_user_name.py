# Generated by Django 4.1.3 on 2022-12-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_pic',
            field=models.ImageField(default='', upload_to='seller/'),
        ),
        migrations.AddField(
            model_name='seller',
            name='user_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
