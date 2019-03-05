#! /bin/bash

# update the vm
sudo apt-get update

# For provision.sh
sudo apt-get install dos2unix

# Install pip3
sudo apt-get install python3-pip -y

# Install mysql server
sudo apt-get install mysql-server -y

# Creates a database
sudo mysql -e "CREATE DATABASE IF NOT EXISTS IAIDSWebsite"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'%' IDENTIFIED BY 'Project1!';"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'vagrant'@'10.0.2.15' IDENTIFIED BY 'Project1!';"
sudo mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'Project1!';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Add IAIDS Django directory inside /var/log/
sudo mkdir /var/log/IAIDSWebsite
sudo chown vagrant /var/log/IAIDSWebsite
mkdir /var/log/IAIDSWebsite/Error

# Makes the images directory
mkdir IAIDSWebsite/images/

# Add extra mysql client stuff
sudo apt-get install libmysqlclient-dev -y

# Instal dependencies for the project
sudo pip3 install -r /home/vagrant/IAIDSWebsite/requirements.txt

# Add firewall rules for django
sudo ufw allow 8000

# Restart after applying mysql settings
sudo service mysql restart
