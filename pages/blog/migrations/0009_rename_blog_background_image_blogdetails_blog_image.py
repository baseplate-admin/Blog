# Generated by Django 3.2.8 on 2021-10-27 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_rename_blog_image_blogdetails_blog_background_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blogdetails",
            old_name="blog_background_image",
            new_name="blog_image",
        ),
    ]
