#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testwork import create_app
import os
import subprocess
import sys

basedir = os.path.abspath(os.path.dirname(__file__))


def main():
    app = create_app()
    app.run()


def start_daemon():
    arg = sys.argv[1:]
    if len(arg):
        url = arg[0]
        subprocess.call('setsid {} {}'.format(os.path.join(basedir, 'client.sh'), url), shell=True)
    else:
        subprocess.call('setsid {}'.format(os.path.join(basedir, 'client.sh')), shell=True)


if __name__ == "__main__":
    main()
