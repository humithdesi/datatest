# Generated by Django 3.2.9 on 2022-01-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dulieu', '0008_auto_20220115_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
