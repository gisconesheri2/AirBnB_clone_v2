#!/usr/bin/python3
"""compress the web_static folder and
distribute the archive to your web server
"""
from fabric.api import local, settings, put, env
from datetime import datetime


def do_pack():
    """add all files in web_static to an archive"""
    cd = datetime.now()

    ymdh = f'{cd.year}{cd.month}{cd.day}{cd.hour}'
    file_name = f'web_static_{ymdh}{cd.minute}{cd.second}.tgz'
    resp_one = local("mkdir -p versions", capture=True)
    resp = local(f"tar -cvzf versions/{file_name} web_static", capture=True)
    if (resp.stderr == ""):
        print(resp.stdout)
        return (f"versions/{file_name}")
    else:
        return (None)

def do_deploy(archive_path):
    """uploads an archive to the remote server, uncompress it
    and set it up to serve content"""
    from os import path

    #env.hosts = ['52.207.9.125', '100.25.171.151']
    is_exists = path.exists(archive_path)

    if (is_exists is False):
        return (False)

    resp = put(archive_path, "/tmp/")
    print(resp.succeeded)
