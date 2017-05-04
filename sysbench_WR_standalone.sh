#!/bin/bash

#Exécuter la commande 5 fois

for i in 1 2 3 4 5
do

##Prepare a test table
sysbench --test=oltp --oltp-table-size=1000000 --mysql-host=172.31.14.30 --mysql-db=tp3db --mysql-user=root --mysql-password=ikograce11 --db-driver=mysql --mysql-table-engine=innodb prepare

##Read/Write test
sysbench --test=oltp --oltp-table-size=1000000 --mysql-host=172.31.14.30 --mysql-db=tp3db --mysql-user=root --mysql-password=ikograce11 --max-time=60 --oltp-test-mode=complex --oltp-read-only=off --max-requests=0 --num-threads=8 --db-driver=mysql run 

##Cleanup table
sysbench --test=oltp --mysql-db=tp3db --db-driver=mysql --mysql-host=172.31.14.30 --mysql-user=root --mysql-password=ikograce11 --mysql-table-engine=innodb cleanup

done
