#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Installs Nginx if not already installed
if ! command -v nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Ensures Nginx is running
sudo service nginx start

# Creates necessary folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creates a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Creates a symbolic link, force delete if already exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gives ownership of /data/ folder to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Updates Nginx configuration
sudo sed -i '/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Tests Nginx configuration and restart if successful
sudo nginx -t && sudo service nginx restart

# Exits successfully
exit 0
