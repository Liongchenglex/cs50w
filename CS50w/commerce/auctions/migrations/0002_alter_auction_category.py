# Generated by Django 3.2.7 on 2021-09-23 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('home', 'HOME'), ('sports', 'SPORTS'), ('clothings', 'CLOTHINGS'), ('books', 'BOOKS'), ('others', 'OTHERS')], max_length=10),
        ),
    ]
