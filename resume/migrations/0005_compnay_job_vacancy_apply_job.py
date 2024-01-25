# Generated by Django 4.2.1 on 2024-01-19 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_remove_job_vacancy_c_id_delete_apply_job_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='compnay',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=50)),
                ('c_email', models.EmailField(max_length=50)),
                ('c_password', models.CharField(max_length=50)),
                ('c_location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='job_vacancy',
            fields=[
                ('jv_id', models.AutoField(primary_key=True, serialize=False)),
                ('jv_name', models.CharField(max_length=50)),
                ('jv_date', models.DateField()),
                ('jv_description', models.TextField(max_length=500)),
                ('jv_location', models.CharField(max_length=50)),
                ('jv_no_of_vacancy', models.IntegerField(default=0)),
                ('jv_eligibility', models.CharField(max_length=50)),
                ('jv_exprince', models.CharField(max_length=50)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.compnay')),
            ],
        ),
        migrations.CreateModel(
            name='apply_job',
            fields=[
                ('aj_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_date', models.DateField()),
                ('resume', models.FileField(default='', upload_to='resume')),
                ('jv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.job_vacancy')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.user_t')),
            ],
        ),
    ]
