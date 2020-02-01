# Generated by Django 2.2.9 on 2020-02-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20200201_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('license_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(related_name='cars', to='rest.Driver'),
        ),
    ]
