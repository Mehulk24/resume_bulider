# Generated by Django 4.2.1 on 2024-01-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0019_remove_templates_t_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates',
            name='t_img',
            field=models.FileField(default='', upload_to='t_img/'),
        ),
    ]
