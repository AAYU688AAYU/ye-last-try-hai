# Generated by Django 5.2.3 on 2025-06-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_bloodtest_colorblindtest'),
    ]

    operations = [
        migrations.AddField(
            model_name='colorblindtest',
            name='erg_data',
            field=models.FileField(blank=True, null=True, upload_to='erg_data/'),
        ),
    ]
