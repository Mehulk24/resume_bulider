# Generated by Django 4.2.1 on 2024-02-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0023_job_vacancy_apply_job_jv_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_vacancy',
            name='jv_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]