# Generated by Django 4.2.1 on 2024-02-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0035_user_t_u_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_t',
            name='r_pdf',
            field=models.FileField(default='', upload_to='r_pdf/'),
        ),
    ]
