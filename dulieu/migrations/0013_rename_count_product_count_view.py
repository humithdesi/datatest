# Generated by Django 3.2.9 on 2022-02-02 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dulieu', '0012_auto_20220202_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='count',
            new_name='count_view',
        ),
    ]
