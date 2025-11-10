import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://inrc230010.github.io/github-pages-cicd-LucasGFP"
RELATIVE_URLS = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
DELETE_OUTPUT_DIRECTORY = True

# Arquivos estáticos
STATIC_PATHS = ['images', 'extra', 'css', 'theme/notmyidea-cms/images']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Descomente se quiser usar Disqus ou Google Analytics
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
