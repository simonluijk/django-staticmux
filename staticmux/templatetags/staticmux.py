# -*- coding: UTF-8 -*-

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders

from ..conf import settings as sm_settings
from ..utils import get_file_urls


register = template.Library()


@register.simple_tag
def static_css(file_name=None, media=None):
    """
    Insert css file with html link element. If DEBUG is True each file
    will be imported individually.

    Insert all files in STATICMUX_CSS:
    {% static_css %}
    
    Insert a specific file:
    {% static_css "css/compressed.css" %}

    Insert a specific file with media attribute:
    {% static_css "css/compressed.css" "print" %}
    """

    if media:
        link_format = '<link rel="stylesheet" type="text/css" href="%%s%%s" media="%s">\n' % media
    else:
        link_format = '<link rel="stylesheet" type="text/css" href="%s%s">\n'
    return _outputfiles(sm_settings.STATICMUX_CSS, file_name, link_format, 'css')


@register.simple_tag
def static_js(file_name=None):
    """
    Insert js file with html script element. If STATICMUX_DEBUG is True each file
    will be imported individually.

    Insert all files in STATICMUX_JS:
    {% static_js %}
    
    Insert a specific file:
    {% static_js "js/compressed.js" %}
    """

    script_format = '<script type="text/javascript" src="%s%s"></script>\n'
    return _outputfiles(sm_settings.STATICMUX_JS, file_name, script_format, 'js')


def _outputfiles(conf, file_name, template_str, ext):
    """
    Helper function for above template tags
    """

    if file_name:
        conf[file_name]
        files = [file_name]
    else:
        files = conf.keys()

    output = u""
    if sm_settings.STATICMUX_DEBUG:
        for file_name in files:
            for file_name in get_file_urls(conf[file_name], ext):
                output += template_str % (settings.STATIC_URL, file_name)
    else:
        for file_name in files:
            key_path = u"%s.key" % finders.find(file_name, all=False)
            key = unicode(open(key_path, 'r').read(), encoding='utf-8').strip()
            file_name = u"%s?key=%s" % (file_name, key)
            output += template_str % (settings.STATIC_URL, file_name)
    return output.strip()

