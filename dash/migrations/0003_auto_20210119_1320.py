# Generated by Django 3.1.5 on 2021-01-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_auto_20210118_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertracker',
            name='visited_mikumi',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertracker',
            name='visited_ngorongoro',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertracker',
            name='visited_selou',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertracker',
            name='visited_serengeti',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
