# Generated by Django 4.1.2 on 2022-10-21 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_dashboard_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('student_id', models.CharField(max_length=100)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('batch', models.CharField(blank=True, max_length=200, null=True)),
                ('is_student', models.BooleanField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/backend/student_profile/')),
            ],
        ),
    ]
