# Generated by Django 5.1.2 on 2024-11-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_alter_skills_text_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='text_field',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]
