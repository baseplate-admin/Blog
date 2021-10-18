from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .snippets import Category

# Create Orderables here


@register_snippet(Category)
class CategoryOrderable(Orderable):
    page = ParentalKey("blog.BlogDetails", related_name="blog_category")
    category = models.ForeignKey("blog.Category", on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel("category"),
    ]
