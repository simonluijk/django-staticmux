# -*- coding: UTF-8 -*-

from django.conf import settings

STATICMUX_DEBUG = getattr(settings, 'STATICMUX_DEBUG', settings.DEBUG)

STATICMUX_JS = getattr(settings, 'STATICMUX_JS', {
    'js/compressed.js': {
        'src': ['js/src',]
    }
})

STATICMUX_JS_FILTERS = getattr(settings, 'STATICMUX_JS_FILTERS', [
    'staticmux.filters.gcompile.Gcompile',
])

STATICMUX_CSS = getattr(settings, 'STATICMUX_CSS', {
    'css/compressed.css': {
        'src': ['css/src',]
    }
})

STATICMUX_CSS_FILTERS = getattr(settings, 'STATICMUX_CSS_FILTERS', [
    'staticmux.filters.cssmin.CSSMin',
])
