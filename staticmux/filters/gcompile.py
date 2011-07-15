# -*- coding: UTF-8 -*-

import subprocess
from django.conf import settings


BINARY = getattr(settings, 'COMPRESS_CLOSURE_BINARY', 'java -jar ~/.bin/compiler.jar')


class Gcompile:
    def process(self, content):
        command = BINARY

        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        p.stdin.write(content.encode('utf-8'))
        p.stdin.close()

        filtered_js = p.stdout.read()
        p.stdout.close()

        err = p.stderr.read()
        p.stderr.close()

        if p.wait() != 0:
            if not err:
                err = 'Unable to apply Google Closure Compiler filter'
            raise Exception(err)

        return filtered_js
