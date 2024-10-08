# Generated by Django 4.2.16 on 2024-09-21 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableOffice',
            fields=[
                ('office_id', models.AutoField(primary_key=True, serialize=False)),
                ('office_desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbloffice',
            },
        ),
        migrations.CreateModel(
            name='TableProcess',
            fields=[
                ('process_id', models.AutoField(primary_key=True, serialize=False)),
                ('office_id', models.IntegerField(default=0)),
                ('process_desc', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tblprocess',
            },
        ),
    ]
