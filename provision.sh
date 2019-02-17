#! /bin/bash

# update the vm
sudo apt-get update

# For provision.sh
sudo apt-get install dos2unix

# Install pip3
sudo apt-get install python3-pip -y

# Install Django
pip3 install django

# Install mysql server
sudo apt-get install mysql-server -y

# Creates a database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS IAIDSWebsite"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'%' IDENTIFIED BY 'Project1!';"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'10.0.2.15' IDENTIFIED BY 'Project1!';"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'Project1!';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Add extra mysql client stuff
sudo apt-get install libmysqlclient-dev -y

# Instal dependencies for the project
pip3 install -r /home/vagrant/IAIDSWebsite/requirements.txt

# Add firewall rules for django
sudo ufw allow 8000

# Restart after applying mysql settings
sudo service mysql restart
