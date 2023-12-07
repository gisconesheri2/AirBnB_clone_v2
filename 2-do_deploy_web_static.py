#!/usr/bin/python3
"""compress the web_static folder and
distribute the archive to your web server
"""
from fabric.api import local, env, put, run
from datetime import datetime
env.hosts = ['52.207.9.125', '100.25.171.151']


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

    is_exists = path.exists(archive_path)

    if (is_exists is False):
        return (False)

    resp = put(archive_path, "/tmp/")

    # strip the 'versions/' string from the archive path
    archive_name = archive_path[archive_path.find('/') + 1:]

    # create the folder name to use by stripping the file type
    folder_name = f"/data/web_static/releases/{archive_name.split('.')[0]}"
    if (resp.suceeded is True):
        resp = run(f"mkdir -p {folder_name}")
    else:
        return (False)

    # uncompress the tar file and delete the archive
    if (resp.succeeded is True):
        resp = run(f"tar -xzf /tmp/{archive_name} -C {folder_name}")
        run(f"rm -f /tmp/{archive_name}")
    else:
        return (False)

    if (resp.succeeded is True):
        # move files to proper position in the folder
        run(f"mv {folder_name}/web_static/* {folder_name}")
        run(f"rm -rf {folder_name}/web_static")

        # delete and create a new symbolic link
        run("rm -rf /data/web_static/current")
        run(f"ln -s {folder_name} /data/web_static/current")
    else:
        return (False)

    return (True)
