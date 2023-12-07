#!/usr/bin/env bash
# set up folders for serving web content

sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

chown ubuntu:ubuntu -Rh /data
echo "
<html>
  <head>
  </head>
  <body>
  	Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
search_string='server_name _;'
alias_hbnb='\\tlocation \/hbnb_static\/ {\n\t\talias \/data/web_static\/current\/;\n}'
sudo sed -i "/$search_string/a $alias_hbnb" /etc/nginx/sites-available/default
sudo service nginx reload
# sudo sed -i "/$search_string/a $replace_string" /etc/haproxy/haproxy.cfg
