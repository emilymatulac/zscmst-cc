# Generated by Django 4.2.14 on 2024-08-01 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0015_alter_evaluation_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_age',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_cc1',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_cc2',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_cc3',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_email',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_region',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_service',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sex',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd0',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd1',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd2',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd3',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd4',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd5',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd6',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd7',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_sqd8',
        ),
        migrations.RemoveField(
            model_name='evaluation',
            name='eval_suggestion',
        ),
    ]
