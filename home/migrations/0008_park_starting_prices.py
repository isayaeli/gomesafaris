# Generated by Django 3.1.5 on 2021-02-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210206_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='starting_prices',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]