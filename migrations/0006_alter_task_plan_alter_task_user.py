# Generated by Django 4.2.6 on 2023-11-08 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0005_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='plan',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='goals.plan'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]