# Generated by Django 2.2.9 on 2020-02-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
