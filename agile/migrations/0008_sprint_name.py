# Generated by Django 3.0.2 on 2020-02-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0007_sprint_backlog_productbacklogid'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='name',
            field=models.TextField(default='Sprint Name'),
        ),
    ]