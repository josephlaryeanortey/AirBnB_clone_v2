#!/usr/bin/python3
"""A module that deploys archives on web servers"""
from fabric.api import local, env, put, run
from time import strftime
from os import path

env.hosts = ['3.90.70.66', '100.26.231.45']


def do_pack():
    """A function that generates .tgz archive from contents of web_static"""
    name = strftime('%Y%m%d%H%M%S')
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(name))
        return ("versions/web_static_{}.tgz".format(name))
    except Exception:
        return None


def do_deploy(archive_path):
    """Function to distribute an archive to web servers"""
    try:
        if not (path.exists(archive_path)):
            return False

        name = archive_path[-18:-4]

        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/web_static_{}/\
                ".format(name))
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C \
                /data/web_static/releases/web_static_{}/".format(name, name))
        run("sudo rm /tmp/web_static_{}.tgz".format(name))
        run("sudo mv /data/web_static/releases/web_static_{}/web_static/* \
                /data/web_static/releases/web_static_{}/".format(name, name))
        run("sudo rm -rf /data/web_static/releases/\
                web_static_{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current".format(name))
    except Exception:
        return False
    return True


def deploy():
    """Function that deploys archives"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
