# Generated by Django 4.2.1 on 2024-02-22 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0033_alter_user_t_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_t',
            name='resume',
        ),
    ]
