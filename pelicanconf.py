AUTHOR = "Baseplate-Admin"
SITENAME = "Blog"
SITEURL = ""
GITHUB_ISSUE_URL = 'https://github.com/baseplate-admin/Blog/issues'

SUBTITLE = "Baseplate Admin's Blog"
SUBTEXT = """This is a place where I document my thoughths
about <b>world</b>, <b>software</b> and things around me
"""
COPYRIGHT = "©2023"
PATH = "content"
THEME = "themes/Papyrus"
TIMEZONE = "Asia/Dhaka"
THEME_STATIC_PATHS = ["static"]
DEFAULT_LANG = "en"
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "sitemap",
    "readtime",
    "search",  # Cant install on windows
    "neighbors",
    "pelican-toc",
]

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (
    "index",
    "search",
    "tags",
    "categories",
    "archives",
)
PAGINATED_TEMPLATES = {
    "index": None,
    "tag": None,
    "category": None,
    "author": None,
    "archives": 24,
}

# Site search plugin

# Table of Content Plugin
TOC = {
    "TOC_HEADERS": "^h[1-3]",  # What headers should be included in
    # the generated toc
    # Expected format is a regular expression
    "TOC_RUN": "true",  # Default value for toc generation,
    # if it does not evaluate
    # to 'true' no toc will be generated
    "TOC_INCLUDE_TITLE": "false",  # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Modify paths
# https://github.com/getpelican/pelican/discussions/3076#discussioncomment-4477731
ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]
# TEMPLATE_PAGES = {
#     # About page
#     "static_pages/about.html": "about.html",
# }

# Social widget
SOCIAL = {
    ("github", "https://github.com/baseplate-admin/blog/"),
    ("reddit", "https://www.reddit.com/user/BasePlate_Admin/"),
    ("twitter", "https://twitter.com/__baseplate__"),
}

SHARE = {
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
}


DEFAULT_PAGINATION = 8

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {
            "permalink": "True",
        },
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
# Sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.1,
        "indexes": 0.1,
        "pages": 0.1,
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "daily",
    },
}

# https://github.com/getpelican/pelican/issues/2497#issuecomment-453388761
DEFAULT_DATE = "fs"


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
