# Generated by Django 4.1 on 2022-09-21 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_alter_watchlistitem_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistitem',
            name='watched',
            field=models.BooleanField(),
        ),
    ]