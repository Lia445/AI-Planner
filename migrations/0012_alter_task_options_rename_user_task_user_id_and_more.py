# Generated by Django 4.2.6 on 2023-11-08 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
        ('todo', '0011_alter_task_options_remove_task_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='group',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='hours',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='goals.plan'),
        ),
    ]