# Generated by Django 3.2.8 on 2021-10-16 12:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("wagtailforms", "0004_add_verbose_name_plural"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wagtailimages", "0023_add_choose_permissions"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("blog", "0006_alter_category_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="BlogDetailsPage",
            new_name="BlogDetails",
        ),
    ]
