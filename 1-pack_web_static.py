#!/usr/bin/python3
"""compress files in the web_static folder"""
from fabric.api import local, settings
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
