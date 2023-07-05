#!/usr/bin/python3
"""Python module to compress all web static files"""
from fabric.api import local
from time import strftime


def do_pack():
    """A function that generates .tgz archive from contents of web_static"""

    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
