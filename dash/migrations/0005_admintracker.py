# Generated by Django 3.1.5 on 2021-02-16 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dash', '0004_auto_20210216_0422'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_1', models.CharField(blank=True, max_length=100, null=True)),
                ('place_2', models.CharField(blank=True, max_length=100, null=True)),
                ('place_3', models.CharField(blank=True, max_length=100, null=True)),
                ('place_4', models.CharField(blank=True, max_length=100, null=True)),
                ('place_5', models.CharField(blank=True, max_length=100, null=True)),
                ('place_6', models.CharField(blank=True, max_length=100, null=True)),
                ('place_7', models.CharField(blank=True, max_length=100, null=True)),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AdminTracker',
            },
        ),
    ]
