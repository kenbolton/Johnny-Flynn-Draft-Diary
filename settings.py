# -*- coding: utf-8 -*-
# Django settings for draftdiary project.

import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells the app to serve media through django.views.static.serve.
SERVE_MEDIA = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'dev.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "site_media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ugdwqh=6up+du=2+h!--da3e8v62h2mul-8lyh#m#%n$(u04%l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'draftdiary.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'compress',
    

# create your virtualenv for the project
# easy_install pip
# pip install -e <new-env> <new-env>/reqs.txt
    'filebrowser',
    'tinymce',
    'djangodblog',
    'django_extensions',
    'oembed',
    'pagination',
    'threadedcomments',
    'videologue',
    'photologue',
    'tagging',
    
    'videodiary',
    
    'django.contrib.admin',
    'django.contrib.admindocs',
)

FILE_UPLOAD_PERMISSIONS = 0755


TINYMCE_DEFAULT_CONFIG = {
    'mode': "textareas",
    'theme': "advanced",
    'language': "en",
    'skin': "o2k7",
#    'browsers': "gecko",
    'dialog_type': "modal",
    'object_resizing': 'true',
    'cleanup_on_startup': 'true',
    'forced_root_block': "p",
    'remove_trailing_nbsp': 'true',
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "none",
    'theme_advanced_buttons1': "formatselect,styleselect,bold,italic,underline,bullist,numlist,undo,redo,link,unlink,image,code,template,visualchars,fullscreen,pasteword,media,search,replace,charmap",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'theme_advanced_path': 'false',
    'theme_advanced_blockformats': "p,h2,h3,h4,div,code,pre",
    'theme_advanced_styles': "[all] clearfix=clearfix;[p] summary=summary;[div] code=code;[img] img_left=img_left;[img] img_left_nospacetop=img_left_nospacetop;[img] img_right=img_right;[img] img_right_nospacetop=img_right_nospacetop;[img] img_block=img_block;[img] img_block_nospacetop=img_block_nospacetop;[div] column span-2=column span-2;[div] column span-4=column span-4;[div] column span-8=column span-8",
    'width': '700',
    'height': '200',
    'plugins': "safari,advimage,advlink,fullscreen,visualchars,paste,media,template,searchreplace",
    'advimage_styles': "Linksbündig neben Text=img_left;Rechtsbündig neben Text=img_right;Eigener Block=img_block",
    'advlink_styles': "internal (sehmaschine.net)=internal;external (link to an external site)=external",
    'advimage_update_dimensions_onchange': 'true',
    'file_browser_callback': "CustomFileBrowser",
    'relative_urls': 'false',
    'valid_elements' : "" +
    "-p," + 
    "a[href|target=_blank|class]," +
    "-strong/-b," +
    "-em/-i," +
    "-u," + 
    "-ol," + 
    "-ul," + 
    "-li," + 
    "br," + 
    "img[class|src|alt=|width|height]," + 
    "-h2,-h3,-h4," + 
    "-pre," +
    "-code," + 
    "-div",
    'extended_valid_elements': "" + 
    "a[name|class|href|target|title|onclick]," + 
    "img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name]," + 
    "br[clearfix]," + 
    "-p[class<clearfix?summary?code]," + 
    "h2[class<clearfix],h3[class<clearfix],h4[class<clearfix]," + 
    "ul[class<clearfix],ol[class<clearfix]," + 
    "div[class],"
    }

FILEBROWSER_URL_WWW = MEDIA_URL
FILEBROWSER_PATH_SERVER = MEDIA_ROOT
FILEBROWSER_URL_TINYMCE = MEDIA_URL + 'js/tiny_mce/'
FILEBROWSER_PATH_TINYMCE = MEDIA_ROOT + 'js/tiny_mce/'

FLOWPLAYER = MEDIA_URL + "swf/flowplayer.commercial-3.1.1.swf"
#VIDEOLOGUE_FFMPEG defaults to ffmpeg
VIDEOLOGUE_FLVTOOL  = None
VIDEOLOGUE_VIDEO_SIZE = "640x352"
VIDEOLOGUE_IMAGE_SIZE = "640x352"
#VIDEOLOGUE_AUDIO_CODEC defaults to libmp3lame
#VIDEOLOGUE_AUDIO_BITRATE defaults to 32000
#VIDEOLOGUE_AUDIO_SAMPLING_RATE defaults to 22050
ADD_THIS_USERNAME = 'kenbolton'

AKISMET_API_KEY = '9d1b53e822e0' # Dime's API key

import socket

if socket.gethostname() == 'kenneth-l-boltons-macbook-pro.local' or 'ubuntu':
    pass
else:
	from prod_settings import *

#  

COMPRESS = True
COMPRESS_VERSION = True
      

COMPRESS_CSS = {
    'group_one': {
        'source_filenames': ('css/blueprint/screen.css', 'css/blueprint/print.css', 'css/base.css'),
        'output_filename': 'css/one_compressed.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    
    # other CSS groups goes here
}

COMPRESS_JS = {
    'all': {
        'source_filenames': ('js/jquery.min.js', 'js/flowplayer-3.1.1.min.js',
        'js/flowplayer.embed-3.0.2.min.js'),
        'output_filename': 'js/all_compressed.js',
    }
}
