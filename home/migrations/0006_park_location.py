# Generated by Django 3.1.5 on 2021-01-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
