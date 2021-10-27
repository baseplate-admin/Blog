# Generated by Django 3.2.8 on 2021-10-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site_settings", "0002_delete_sitenamesettings"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="socialmediasettings",
            name="main_logo",
        ),
        migrations.RemoveField(
            model_name="socialmediasettings",
            name="youtube",
        ),
        migrations.AddField(
            model_name="socialmediasettings",
            name="github",
            field=models.URLField(blank=True, help_text="Github Url", null=True),
        ),
    ]