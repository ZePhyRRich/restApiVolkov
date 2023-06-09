# Generated by Django 4.0.4 on 2023-04-02 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0006_order_delivery_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.AlterModelOptions(
            name='transport',
            options={'verbose_name': 'Транспорт', 'verbose_name_plural': 'Транспорт'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='retrive_address',
        ),
        migrations.RemoveField(
            model_name='retrivetype',
            name='added_price',
        ),
        migrations.RemoveField(
            model_name='retrivetype',
            name='delivery_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='retrive_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainSite.retrivetype', verbose_name='Тип отправления'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainSite.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transport',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainSite.transport', verbose_name='Транспорт'),
        ),
        migrations.CreateModel(
            name='OrderRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('delivery_time', models.IntegerField(blank=True, null=True, verbose_name='Время доставки')),
                ('from_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_city', to='mainSite.city', verbose_name='Откуда')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='mainSite.order', verbose_name='Заказ')),
                ('to_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_city', to='mainSite.city', verbose_name='Куда')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='from_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_city_order', to='mainSite.city', verbose_name='Откуда'),
        ),
        migrations.AddField(
            model_name='order',
            name='to_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_city_order', to='mainSite.city', verbose_name='Куда'),
        ),
    ]
