# Generated by Django 3.2.8 on 2021-10-16 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("site_settings", "0006_rename_site_name_siteownershipsettings_site_owner"),
    ]

    operations = [
        migrations.RenameField(
            model_name="siteownershipsettings",
            old_name="site_owner",
            new_name="site_name",
        ),
    ]
