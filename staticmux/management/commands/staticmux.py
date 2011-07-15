# -*- coding: UTF-8 -*-

import os
import hashlib

from django.core.management.base import BaseCommand
from django.conf import settings

from ...conf import settings as sm_settings
from ...utils import get_file_paths

try:
    import importlib
except ImportError:
    from django.utils import importlib


def get_content(conf, media_ext):
    """
    Helper to grab and concat content from files
    """

    content = u""
    for media_file in get_file_paths(conf, media_ext):
        content += unicode(open(media_file, 'r').read(), encoding='utf-8')
    return content


def write_static_file(file_name, content):
    """
    Helper to write static file
    """

    fh = open(os.path.join(settings.STATICFILES_DIRS[0], file_name), 'w')
    fh.write(content.encode('utf-8'))
    fh.close()

    key_file = u'%s.key' % file_name
    fh = open(os.path.join(settings.STATICFILES_DIRS[0], key_file), 'w')
    fh.write(hashlib.md5(content).hexdigest().encode('utf-8'))
    fh.close()


def process_filter(static_filter, content):
    """
    Helper function to process a static media filter
    """

    (mod, cls) = static_filter.rsplit('.', 1)
    mod = importlib.import_module(mod)
    cls = getattr(mod, cls)()
    return cls.process(content)


class Command(BaseCommand):
    """
    Management command to multiplex static media
    """
    
    def handle(self, *args, **kwargs):
        for file_name in sm_settings.STATICMUX_CSS.keys():
            content = get_content(sm_settings.STATICMUX_CSS[file_name], 'css')
            for css_filter in sm_settings.STATICMUX_CSS_FILTERS:
                content = process_filter(css_filter, content)
            write_static_file(file_name, content)

        for file_name in sm_settings.STATICMUX_JS.keys():
            content = get_content(sm_settings.STATICMUX_JS[file_name], 'js')
            for js_filter in sm_settings.STATICMUX_JS_FILTERS:
                content = process_filter(js_filter, content)
            write_static_file(file_name, content)

