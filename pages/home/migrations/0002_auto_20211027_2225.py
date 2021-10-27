# Generated by Django 3.2.8 on 2021-10-27 16:25

import custom.blocks.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='author_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='home',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', custom.blocks.blocks.RichtextBlock())], blank=True, null=True),
        ),
    ]
