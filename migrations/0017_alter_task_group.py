# Generated by Django 4.2.6 on 2023-11-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0016_user_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='group',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]