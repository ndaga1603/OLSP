# Generated by Django 4.1.5 on 2023-02-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0006_supervisor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='report',
            new_name='text',
        ),
        migrations.AddField(
            model_name='weeklyreport',
            name='heading',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
