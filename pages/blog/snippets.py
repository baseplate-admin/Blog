from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

# Create Models here


class Category(models.Model):
    name = models.CharField(max_length=100)

    panels = [
        MultiFieldPanel(
            [FieldPanel("name")],
            heading="Category info",
        ),
    ]

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
