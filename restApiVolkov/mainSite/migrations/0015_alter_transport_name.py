# Generated by Django 4.0.4 on 2023-04-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0014_remove_retrivetype_transport_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Наименование'),
        ),
    ]
