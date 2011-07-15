# -*- coding: UTF-8 -*-

import os
from django.contrib.staticfiles import finders


def get_files(config, media_ext):
    """
    Worker function for the helpers below
    """

    # TODO: Only return files that have an extention that matched ext
    files = []
    for src in config['src']:
        src_path = finders.find(src, all=False)
        if os.path.isdir(src_path):
            for file_name in sorted(os.listdir(src_path)):
                files.append([
                    u"%s/%s" % (src_path, file_name),
                    u"%s/%s" % (src, file_name)
                ])
        elif os.path.isfile(src_path):
            files.append([src_path, src])
    return files


def get_file_urls(config, media_ext):
    """
    Helper to get a list of file urls from a config list.
    """

    return [src for src_path, src in get_files(config, media_ext)]


def get_file_paths(config, media_ext):
    """
    Helper to get a list of file paths from a config list.
    """

    return [src_path for src_path, src in get_files(config, media_ext)]
