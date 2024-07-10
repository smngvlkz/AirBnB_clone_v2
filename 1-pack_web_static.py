#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Creates the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generates the archive name with timestamp
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(date)

        # Creates the archive
        local("tar -cvzf {} web_static".format(archive_name))

        # Checks if the archive was created successfully
        if os.path.exists(archive_name):
            return archive_name
        else:
            return None
    except:
        return None
