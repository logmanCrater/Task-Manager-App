# Generated by Django 5.0.7 on 2024-07-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_remove_userprofile_is_ceo_remove_userprofile_is_dev_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_ceo',
            field=models.BooleanField(default=False, verbose_name='CEO'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_dev',
            field=models.BooleanField(default=False, verbose_name='DEV'),
        ),
    ]