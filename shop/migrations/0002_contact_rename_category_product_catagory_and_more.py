# Generated by Django 4.0.6 on 2022-07-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='catagory',
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=0, help_text='0-Show,1-Hidden'),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner_number',
            field=models.BigIntegerField(unique=True),
        ),
    ]
