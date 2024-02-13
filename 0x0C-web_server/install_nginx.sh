#!/bin/bash

# Install Nginx
apt-get update
apt-get install -y nginx

# Start Nginx service
service nginx start

# Configure Nginx to listen on port 80
sed -i 's/listen 80 default_server;/listen 80;/g' /etc/nginx/sites-available/default

# Replace the default index.html file with a custom page
echo "Hello World!" > /var/www/html/index.html

# Restart Nginx
service nginx restart
