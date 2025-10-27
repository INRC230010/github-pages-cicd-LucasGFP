AUTHOR = 'Lucas'
SITENAME = 'Meu Site'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_BR'
LOCALE = ('pt_BR.UTF-8', 'pt_BR', 'pt')
DATE_FORMATS = {'pt': ('%d/%m/%Y')}

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
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/LucasGFP"),
    ("LinkedIn", "https://www.linkedin.com/in/lucas-godoy-a0942331a/"),
)

DEFAULT_PAGINATION = False

THEME = 'pelican-themes/notmyidea-cms'


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
