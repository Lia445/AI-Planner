# Generated by Django 4.2.6 on 2023-11-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_user_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
