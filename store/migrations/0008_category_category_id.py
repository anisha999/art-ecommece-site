# Generated by Django 2.2.14 on 2020-12-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20201210_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
    ]
