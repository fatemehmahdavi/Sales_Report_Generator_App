# Generated by Django 4.1 on 2022-09-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_rename_csv_file_csv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
