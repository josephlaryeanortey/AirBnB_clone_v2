#!/usr/bin/python3
"""Python module to compress all web static files"""
from fabric.api import local
from time import strftime
import os


def do_pack():
    """A function that generates .tgz archive from contents of web_static"""

    name = strftime('%Y%m%d%H%M%S')
    archive_path = "versions/web_static_{}.tgz".format(name)
    print("Packing web_static to {}".format(archive_path))

    try:
        os.makedirs("versions")
    except OSError:
        return None

    result = local("tar -czvf versions/web_static_{}.tgz web_static"
                   .format(name))
    archive_size = os.path.getsize(archive_path)
    print("web_static packed: {} -> {}Bytes".format(archive_path,
          archive_size))

    if result.stdout.strip() == '0':
        return ("versions/web_static_{}.tgz".format(name))
    else:
        return None
