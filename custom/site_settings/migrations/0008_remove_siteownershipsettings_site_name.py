# Generated by Django 3.2.8 on 2021-10-16 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("site_settings", "0007_rename_site_owner_siteownershipsettings_site_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="siteownershipsettings",
            name="site_name",
        ),
    ]