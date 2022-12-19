# Generated by Django 4.1.4 on 2022-12-17 15:13

import billing.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('from_date', models.DateField(auto_now=True)),
                ('to_date', models.DateField()),
                ('amount', models.FloatField(validators=[billing.models.validate_amount])),
                ('status', models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid')], max_length=40)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.customer')),
            ],
        ),
    ]