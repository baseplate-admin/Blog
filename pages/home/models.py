from wagtail.core.models import Page
from wagtailcache.cache import WagtailCacheMixin
from django.db import models
from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
)
from custom.blocks import blocks
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.


class Home(WagtailCacheMixin, Page):
    max_count = 1
    subpage_types = [
        "blog.BlogList",  # appname.ModelName
    ]

    parent_page_type = ["wagtailcore.Page"]  # appname.ModelName

    class Meta:
        verbose_name = "Home"

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [
            ("full_richtext", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        ImageChooserPanel("author_image"),
        StreamFieldPanel("content"),
    ]
