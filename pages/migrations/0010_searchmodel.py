# Generated by Django 4.1.5 on 2023-03-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_patient_doctor_alter_patient_patient_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]