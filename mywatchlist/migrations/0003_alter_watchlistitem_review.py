# Generated by Django 4.1 on 2022-09-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_watchlistitem_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='review',
            field=models.CharField(max_length=60),
        ),
    ]
