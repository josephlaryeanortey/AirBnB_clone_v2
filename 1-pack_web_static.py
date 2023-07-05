#!/usr/bin/python3
"""Python module to compress all web static files"""
from fabric.api import local
from time import strftime


def do_pack():
    """A function that generates .tgz archive from contents of web_static"""
    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception:
        return None
