#!/usr/bin/python3
# Distributes an archive to web servers using Fabric

from fabric.api import env, put, run
import os

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = 'path/to/your/private/key'

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Extracts the archive file name without extension
        file_name = os.path.basename(archive_path)
        no_ext = file_name.split('.')[0]

        # Uploads the archive to /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # Creates the target directory
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))

        # Uncompresses the archive to the folder
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_name, no_ext))

        # Deletes the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Moves the contents to the appropriate directory
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(no_ext, no_ext))

        # Deletes the web_static folder inside the release folder
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))

        # Deletes the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Creates a new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
