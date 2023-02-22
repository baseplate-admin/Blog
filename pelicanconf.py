AUTHOR = "Baseplate-Admin"
SITENAME = "Blog"
# SITEURL = "https://baseplate-admin.github.io/blog"
SITEURL = ""

SUBTITLE = "Papyrus"
SUBTEXT = """A fast and responsive theme built for the <a class="underline" 
href="https://blog.getpelican.com/">Pelican</a> site generator.<br>
The theme is inspired from <a class="underline" 
href="https://github.com/adityatelange/hugo-PaperMod">Hugo-PaperMod</a>. 
It is styled using <a class="underline" 
href="https://tailwindcss.com/">Tailwind CSS</a>. 
It supports dark mode and built in search function.
"""
COPYRIGHT = "©2023"
PATH = "content"
THEME = "themes/Papyrus"
TIMEZONE = 'Asia/Dhaka'
THEME_STATIC_PATHS = ["static"]
DEFAULT_LANG = "en"
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    "readtime",
    # "search", # Cant install on windows
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
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
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

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
