# Generated by Django 3.2.8 on 2021-10-15 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("site_settings", "0005_rename_sitenamesettings_siteownershipsettings"),
    ]

    operations = [
        migrations.RenameField(
            model_name="siteownershipsettings",
            old_name="site_name",
            new_name="site_owner",
        ),
    ]
