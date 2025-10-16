AUTHOR = 'Tomislav Suhina'
SITENAME = 'Tomislav Suhina - Freelance Decision Scientist'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - empty to remove default links
LINKS = ()

# Social widget - empty to remove default links
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SITEURL = ''
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']

# Template overrides for custom modifications
THEME_TEMPLATES_OVERRIDES = ['templates']

# Page configuration
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Index page configuration - move blog index to /blog/
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/index.html'

# Article configuration
ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'

# Menu items
MENUITEMS = [
    ('About', '/'),
    ('Services', '/services.html'),
    ('Experience', '/experience.html'),
    ('Projects', '/projects.html'),
    ('Blog', '/blog/'),
    ('Contact', '/contact.html'),
]