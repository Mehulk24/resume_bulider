# Generated by Django 4.2.1 on 2024-02-17 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0027_remove_apply_job_a_date_apply_job_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply_job',
            name='c_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resume.company'),
            preserve_default=False,
        ),
    ]
