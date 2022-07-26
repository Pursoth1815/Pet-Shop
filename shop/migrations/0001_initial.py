# Generated by Django 4.0.6 on 2022-07-14 16:50

from django.db import migrations, models
import django.db.models.deletion
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=150)),
                ('pet_name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
                ('owner_number', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catagory')),
            ],
        ),
    ]
