# Generated by Django 3.1.5 on 2021-02-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_auto_20210119_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertracker',
            name='visited_mikumi',
        ),
        migrations.RemoveField(
            model_name='usertracker',
            name='visited_ngorongoro',
        ),
        migrations.RemoveField(
            model_name='usertracker',
            name='visited_selou',
        ),
        migrations.RemoveField(
            model_name='usertracker',
            name='visited_serengeti',
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usertracker',
            name='place_7',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
