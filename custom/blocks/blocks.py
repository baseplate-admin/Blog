"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    class Meta:  # noqa
        template = "blocks/rich_text_block.html"
        icon = "doc-full"
        label = "Full RichText"
