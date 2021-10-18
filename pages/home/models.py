from wagtail.core.models import Page

# Create your models here.


class Home(Page):
    max_count = 1
    subpage_types = [
        "blog.BlogList",  # appname.ModelName
    ]

    parent_page_type = ["wagtailcore.Page"]  # appname.ModelName

    class Meta:
        verbose_name = "Home"
