# Generated by Django 4.2.6 on 2023-12-01 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0018_alter_task_user_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
