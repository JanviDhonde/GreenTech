# Generated by Django 3.2.4 on 2024-03-18 09:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0023_rename_userprofiles_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UsrProfile',
        ),
    ]