# Generated by Django 3.2 on 2022-01-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schedular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_email_id', models.CharField(max_length=60, verbose_name='Staff Email ID')),
                ('associated_program_code', models.CharField(default='qwerty', max_length=255, null=True, verbose_name='Associated Program Code')),
                ('academic_year_code', models.CharField(default='qwerty', max_length=255, null=True, verbose_name='Academic Year Code')),
                ('batch', models.CharField(blank=True, max_length=255, null=True, verbose_name='Batch')),
                ('semester', models.CharField(max_length=255, verbose_name='Semester')),
                ('class_type', models.CharField(choices=[('LECTURE', 'LECTURE'), ('TUTORIAL', 'TUTORIAL'), ('PRACTICAL', 'PRACTICAL')], max_length=255, verbose_name='Class Type')),
                ('day', models.CharField(choices=[('MON', 'MON'), ('TUE', 'TUE'), ('WED', 'WED'), ('THU', 'THU'), ('FRI', 'FRI'), ('SAT', 'SAT')], max_length=255, verbose_name='Day')),
                ('venue', models.CharField(max_length=255, verbose_name='Venue')),
                ('start_time', models.CharField(max_length=255, verbose_name='Start Time')),
                ('end_time', models.CharField(max_length=255, verbose_name='End Time')),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=255, verbose_name='Status')),
            ],
        ),
    ]
