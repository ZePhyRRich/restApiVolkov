# Generated by Django 4.0.4 on 2023-04-02 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='retrivetype',
            name='transport_type',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='transport_type',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='RetriveType',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='Transport',
        ),
        migrations.DeleteModel(
            name='Transport_Type',
        ),
    ]
