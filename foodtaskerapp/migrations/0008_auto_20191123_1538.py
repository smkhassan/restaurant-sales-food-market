# Generated by Django 2.2.7 on 2019-11-23 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0007_driver_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodtaskerapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodtaskerapp.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='foodtaskerapp.Driver'),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodtaskerapp.Restaurant'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='foodtaskerapp.Meal'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_details', to='foodtaskerapp.Order'),
        ),
    ]
