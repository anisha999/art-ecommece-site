# Generated by Django 2.2.14 on 2020-12-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20201217_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=500),
        ),
    ]