# -*- coding: UTF-8 -*-

from ..filters.cssmin import cssmin


class CSSMin:
    def process(self, content):
        return cssmin(content)
