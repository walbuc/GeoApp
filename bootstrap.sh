#!/usr/bin/env bash

apt-get update
apt-get -y upgrade

apt-get install -y git subversion curl vim screen ssh
apt-get install -y lynx links links2

######################### apache2 #########################
apt-get install -y apache2
rm -rf /var/www
ln -fs /vagrant /var/www

apt-get install -y libapache2-mod-wsgi

######################### Python #########################
apt-get -y install python-pip python2.7 build-essential python-virtualenv

######################### MySQL #########################
MYSQL_PASSWORD="django"

echo "mysql-server-5.5 mysql-server/root_password password $MYSQL_PASSWORD" | debconf-set-selections
echo "mysql-server-5.5 mysql-server/root_password_again password $MYSQL_PASSWORD" | debconf-set-selections

apt-get -y install mysql-client mysql-server sqlite3
apt-get -y install python-mysqldb libmysqlclient-dev python-mysql.connector python3-mysql.connector

######################### Restart services #########################

service apache2 restart
service mysql restart

##### Django #####

pip install Django==1.7.7
pip install MySQL-python

echo "All Done"
