# Generated by Django 5.1.3 on 2024-11-18 14:40

import sorl.thumbnail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('background_image', sorl.thumbnail.fields.ImageField(upload_to='')),
            ],
        ),
    ]
