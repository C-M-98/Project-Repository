# Generated by Django 5.1.2 on 2024-11-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_styles_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
