# Generated by Django 5.1.2 on 2024-11-29 13:30

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0013_education_certificate_edustyles_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='certificate',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]
