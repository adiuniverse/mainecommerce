# Generated by Django 4.1.3 on 2022-12-17 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_seller_seller_pic_seller_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('number', models.BigIntegerField()),
                ('price', models.FloatField()),
                ('stock', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
    ]
