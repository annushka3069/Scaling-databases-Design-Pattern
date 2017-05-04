#!/bin/bash
output clear

#Required updates and installations
sudo apt-get update -y 
sudo apt-get upgrade -y 
sudo apt-get -y install libaio1 

#Download and install MySQL cluster
wget https://dev.mysql.com/get/Downloads/MySQL-Cluster-7.4/mysql-cluster-gpl-7.4.15-debian8-x86_64.deb
sudo dpkg -i mysql-cluster-gpl-7.4.15-debian8-x86_64.deb

#Link mysql server to /usr/local/mysql server
sudo ln -s /opt/mysql/server-5.6/ /usr/local/mysql

#Make relevant commands available
export PATH=$PATH:/usr/local/mysql/bin
sudo echo "export PATH=\$PATH:/usr/local/mysql/bin" >> /etc/bash.bashrc
sudo cp /usr/local/mysql/bin/ndb_mgm* /usr/local/bin

#Copy the configuration file for management node
sudo mkdir /var/lib/mysql-cluster
sudo cp /var/tmp/config.ini /var/lib/mysql-cluster

