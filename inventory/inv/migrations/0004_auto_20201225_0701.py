# Generated by Django 3.1.4 on 2020-12-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0003_auto_20201225_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_updated',
            field=models.DateTimeField(),
        ),
    ]