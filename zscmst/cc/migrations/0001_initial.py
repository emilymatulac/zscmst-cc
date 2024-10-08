# Generated by Django 4.2.16 on 2024-09-13 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenCharter',
            fields=[
                ('eval_id', models.AutoField(primary_key=True, serialize=False)),
                ('eval_citizenttype', models.CharField(default='', max_length=50)),
                ('eval_date', models.CharField(default='', max_length=50)),
                ('eval_sex', models.CharField(default='0', max_length=1)),
                ('eval_age', models.IntegerField()),
                ('eval_region', models.CharField(default='', max_length=30)),
                ('eval_service', models.CharField(default='', max_length=30)),
                ('eval_cc1', models.IntegerField(default=0)),
                ('eval_cc2', models.IntegerField(default=0)),
                ('eval_cc3', models.IntegerField(default=0)),
                ('eval_sqd0', models.IntegerField(default=0)),
                ('eval_sqd1', models.IntegerField(default=0)),
                ('eval_sqd2', models.IntegerField(default=0)),
                ('eval_sqd3', models.IntegerField(default=0)),
                ('eval_sqd4', models.IntegerField(default=0)),
                ('eval_sqd5', models.IntegerField(default=0)),
                ('eval_sqd6', models.IntegerField(default=0)),
                ('eval_sqd7', models.IntegerField(default=0)),
                ('eval_sqd8', models.IntegerField(default=0)),
                ('eval_suggestion', models.CharField(default='', max_length=250)),
                ('eval_email', models.CharField(default='', max_length=30)),
                ('eval_name', models.CharField(default='', max_length=30)),
            ],
            options={
                'db_table': 'tblcitizen',
            },
        ),
    ]
