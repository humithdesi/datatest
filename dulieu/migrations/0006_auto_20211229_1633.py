# Generated by Django 3.2.9 on 2021-12-29 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dulieu', '0005_auto_20211229_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='loaiGa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dulieu.loaiga'),
        ),
        migrations.AlterField(
            model_name='product',
            name='loaiNem',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dulieu.loainem'),
        ),
    ]
