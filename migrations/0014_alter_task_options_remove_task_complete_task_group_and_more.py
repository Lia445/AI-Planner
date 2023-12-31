# Generated by Django 4.2.6 on 2023-11-09 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
        ('todo', '0013_alter_task_options_remove_task_group_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['status']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='complete',
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
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NOT STARTED', 'Not Started'), ('DOING', 'Doing'), ('DONE', 'Done')], default='NOT STARTED', max_length=12),
        ),
    ]
