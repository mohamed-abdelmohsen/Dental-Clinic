# Generated by Django 4.1.5 on 2023-03-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_delete_patient_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='session',
            field=models.TextField(null=True),
        ),
    ]