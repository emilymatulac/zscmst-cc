# Generated by Django 4.2.14 on 2024-07-31 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='eval_age',
            field=models.IntegerField(default=0, max_length=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_cc1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_cc2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_cc3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_cc4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_cc5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_email',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_region',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_service',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sex',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd0',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_sqd8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='eval_suggestion',
            field=models.CharField(default=' ', max_length=250),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='eval_citizenttype',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterModelTable(
            name='evaluation',
            table='tblcsmq',
        ),
    ]
