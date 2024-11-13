# Generated by Django 3.2.4 on 2024-03-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_customerlogin_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerlogin',
            name='gender',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='contact_number',
            field=models.CharField(default=1212, max_length=15),
            preserve_default=False,
        ),
    ]