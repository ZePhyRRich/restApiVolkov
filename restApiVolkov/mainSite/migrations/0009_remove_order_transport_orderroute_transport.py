# Generated by Django 4.0.4 on 2023-04-02 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0008_remove_order_total_price_remove_transport_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transport',
        ),
        migrations.AddField(
            model_name='orderroute',
            name='transport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainSite.transport', verbose_name='Транспорт'),
        ),
    ]
