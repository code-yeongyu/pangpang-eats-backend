# Generated by Django 3.2.5 on 2021-07-05 07:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=5)),
                ('business_name', models.CharField(max_length=40)),
                ('business_registration_number', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='menu_pictures')),
                ('price', models.PositiveIntegerField()),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('picture', models.ImageField(upload_to='store_pictures')),
                ('minimum_order_cost', models.IntegerField()),
                ('minimum_delivery_cost', models.IntegerField()),
                ('telephone_number', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(9)])),
                ('description', models.TextField()),
                ('notice', models.TextField()),
                ('origin_information', models.TextField()),
                ('nuturition_facts', models.TextField()),
                ('allergens_facts', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_information', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='store.businessinformation')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='store.location')),
            ],
        ),
    ]
