# Generated by Django 4.0 on 2022-03-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
