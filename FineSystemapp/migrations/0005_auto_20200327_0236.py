# Generated by Django 3.0.3 on 2020-03-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FineSystemapp', '0004_auto_20200322_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_fine',
            name='Date',
            field=models.DateField(),
        ),
    ]
