from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text="Facebook Url")
    github = models.URLField(blank=True, null=True, help_text="Github Url")
    email = models.URLField(blank=True, null=True, help_text="Email Url")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("github"),
                FieldPanel("email"),
            ],
            heading="Social Media Settings",
        )
    ]


@register_setting
class SiteOwnerShipSettings(BaseSetting):
    site_name = models.CharField(max_length=30)
    copyright = models.CharField(max_length=30)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_name"),
                FieldPanel("copyright"),
            ]
        )
    ]
