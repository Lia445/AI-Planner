# Generated by Django 4.2.6 on 2023-12-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0022_alter_task_options_task_date_task_group_task_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]