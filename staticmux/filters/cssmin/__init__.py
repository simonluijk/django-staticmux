# -*- coding: UTF-8 -*-

from .cssmin import cssmin


class CSSMin(object):
    def process(self, content):
        return cssmin(content)
