# Generated by Django 3.0.2 on 2020-02-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0006_auto_20200223_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint_backlog',
            name='productbacklogID',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
