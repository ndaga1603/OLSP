# Generated by Django 4.1.5 on 2023-01-27 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0003_weeklyreport_dairyreport'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DairyReport',
            new_name='DailyReport',
        ),
        migrations.RenameField(
            model_name='dailyreport',
            old_name='workin_hours',
            new_name='working_hours',
        ),
    ]
