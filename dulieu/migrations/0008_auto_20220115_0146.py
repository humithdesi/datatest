# Generated by Django 3.2.9 on 2022-01-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dulieu', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
