# Generated by Django 5.0.7 on 2024-07-12 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_userprofile_is_ceo_userprofile_is_dev'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
