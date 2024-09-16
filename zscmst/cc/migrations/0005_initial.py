# Generated by Django 4.2.14 on 2024-07-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cc', '0004_delete_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('eval_id', models.AutoField(primary_key=True, serialize=False)),
                ('eval_citizenttype', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tblevaluation',
            },
        ),
    ]
