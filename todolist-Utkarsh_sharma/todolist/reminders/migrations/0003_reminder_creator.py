# Generated by Django 4.0 on 2022-03-04 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('reminders', '0002_reminder_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='creator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
