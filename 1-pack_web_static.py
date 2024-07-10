#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Creates the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")
    
    # Creates the archive name
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    
    # Creates the archive
    result = local("tar -cvzf {} web_static".format(archive_name))
    
    # Checks if the archive was created successfully
    if result.succeeded:
        return archive_name
    else:
        return None
