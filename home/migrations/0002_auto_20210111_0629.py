# Generated by Django 3.1.5 on 2021-01-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterField(
            model_name='country',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='image',
            field=models.ImageField(upload_to='country_images'),
        ),
    ]
