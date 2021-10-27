# Generated by Django 3.2.8 on 2021-10-16 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("site_settings", "0010_delete_siteownershipsettings"),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteOwnerShipSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_name", models.CharField(max_length=30)),
                ("copyright", models.CharField(max_length=30)),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]