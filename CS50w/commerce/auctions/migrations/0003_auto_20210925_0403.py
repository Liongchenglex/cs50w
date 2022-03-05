# Generated by Django 3.2.7 on 2021-09-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_auction_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bids',
            options={'verbose_name_plural': 'Bids'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('-time',)},
        ),
        migrations.AddField(
            model_name='auction',
            name='has_ended',
            field=models.BooleanField(default=False),
        ),
    ]
