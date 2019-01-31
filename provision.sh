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

# got to the correct directory
cd IAIDSWebsite/

# migrate data to mysql server
python3 manage.py migrate

# Add firewall rules for django
sudo ufw allow 8000

# Go back a directory
cd ..

# Adds mysql configuration
printf "[mysqld]\nbind-address = 0.0.0.0\n\n" >> /etc/mysql/my.cnf 

# Restart after applying mysql settings
sudo service mysql restart
