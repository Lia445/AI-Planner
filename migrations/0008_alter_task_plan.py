# Generated by Django 4.2.6 on 2023-11-08 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
        ('todo', '0007_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goals.plan'),
        ),
    ]
