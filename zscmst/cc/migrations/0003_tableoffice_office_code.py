# Generated by Django 4.2.16 on 2024-09-21 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0002_tableoffice_tableprocess'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableoffice',
            name='office_code',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
