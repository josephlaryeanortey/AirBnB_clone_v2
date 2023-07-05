#!/usr/bin/python3
"""Python module to deploy archive on web servers"""
from fabric.api import env, put, run, sudo
from os import path

env.hosts = ['3.90.70.66', '100.26.231.45']


def do_deploy(archive_path):
    """Deploy archive to web server"""
    if path.isfile(archive_path) is False:
        return False
    try:
        f_name = archive_path.split("/")[-1]
        no_ext = f_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(f_name, path_no_ext))
        run("rm /tmp/{}".format(f_name))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))

        return True
    except:
        return False
