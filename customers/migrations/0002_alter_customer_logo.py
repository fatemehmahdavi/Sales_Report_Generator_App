# Generated by Django 4.1 on 2022-09-10 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.FileField(default='no_picture.png', upload_to='customers/'),
        ),
    ]
