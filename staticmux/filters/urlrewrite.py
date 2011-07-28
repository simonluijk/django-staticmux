# -*- coding: UTF-8 -*-

import re


URL_PATT = re.compile("url\((?P<url>[^\)]+)\)")
BAK_PATT = re.compile("^\.\.\/")

def rewrite_url(match):
    url = match.groups()[0].strip('"').strip("'")
    return u"url(%s)" % BAK_PATT.sub("", url)

class UrlRewrite(object):
    def process(self, content):
        return URL_PATT.sub(rewrite_url, content)
