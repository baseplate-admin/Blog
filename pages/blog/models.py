from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtailcache.cache import WagtailCacheMixin

from .orderables import *
from custom.blocks import blocks


# Create your pages here.


class BlogList(WagtailCacheMixin, Page):
    # template = "blog/blog_page.html"
    max_count = 1
    parent_page_type = ["home.Home"]
    subpage_types = ["blog.BlogDetails"]

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        all_posts = BlogDetails.objects.live().public().order_by("-first_published_at")

        paginator = Paginator(all_posts, 5)  # @todo add more pages
        page = request.GET.get("page")

        try:
            posts = paginator.page(page)

        except PageNotAnInteger:
            posts = paginator.page(1)

        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        return context


class BlogDetails(WagtailCacheMixin, Page):
    # template = "blog/blog_details_page.html"
    parent_page_type = [
        "blog.BlogList",  # appname.ModelName
    ]
    subpage_types = []

    class Meta:
        verbose_name = "Blog Detail"
        verbose_name_plural = "Blog(s) Detail"

    blog_image = models.ForeignKey(
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
        ImageChooserPanel("blog_image"),
        MultiFieldPanel(
            [InlinePanel("blog_category", label="Category", min_num=1, max_num=1)],
            heading="Author",
        ),
        StreamFieldPanel("content"),
    ]
