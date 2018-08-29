Title: Pelican setup
Date: 2018-08-26 14:00
Category: Setup
Tags: setup, tools, pelican

```
mkdir pelican.site
cd pelican.site
pipenv install pelican markdown
git clone --recursive https://github.com/getpelican/pelican-themes
git clone --recursive https://github.com/getpelican/pelican-plugins
pipenv run make html
pipenv run ./develop_server.sh start
pipenv run ./develop_server.sh stop
```

Edit `pelicanconf.py`:

```
TIMEZONE = 'America/Indiana/Indianapolis'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

PLUGIN_PATHS = ['../pelican-plugins']

PLUGINS = [
        'assets',
]

THEME = '../taman'
# THEME = '../pelican-themes/taman'

# taman theme
USER_LOGO_URL = '/images/JPB_headshot.jpg'
TAGLINE = '''
Data Scientist and Engineer
'''
# end taman theme
```

And then

```
pipenv install webassets cssmin
```
