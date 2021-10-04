# Generated by Django 3.2.7 on 2021-09-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_repeat',
            field=models.CharField(choices=[('No Repeat', 'No Repeat'), ('Once a Day', 'Once a Day'), ('Once a Week', 'Once a Week'), ('Once a Month', 'Once a Month'), ('Once a Year', 'Once a Year')], default='No Repeat', max_length=15),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('Not Completed', 'Not Completed'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Completed', max_length=15),
        ),
    ]
