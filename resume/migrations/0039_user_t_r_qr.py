# Generated by Django 4.2.1 on 2024-02-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0038_alter_user_t_r_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_t',
            name='r_qr',
            field=models.ImageField(default='', upload_to='qr/'),
        ),
    ]