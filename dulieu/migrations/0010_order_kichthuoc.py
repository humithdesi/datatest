# Generated by Django 3.2.9 on 2022-01-16 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dulieu', '0009_auto_20220115_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='kichthuoc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
