# Generated by Django 3.2.9 on 2022-02-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dulieu', '0016_alter_review_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
