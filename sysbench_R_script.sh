#!/bin/bash

#Exécuter la commande 5 fois

for i in 1 2 3 4 5
do

##Prepare a test table
sysbench --test=oltp --oltp-table-size=1000000 --mysql-host=localhost --mysql-db=tp3db --mysql-user=root --mysql-password=ikograce11 --db-driver=mysql --mysql-table-engine=innodb prepare

##Read-Only test
sysbench --test=oltp --oltp-table-size=1000000 --mysql-host=localhost --mysql-db=tp3db --mysql-user=root --mysql-password=ikograce11 --oltp-read-only=on --db-driver=mysql --num-threads=8 --mysql-table-engine=innodb run

##Cleanup table
sysbench --test=oltp --mysql-db=tp3db --db-driver=mysql --mysql-host=localhost --mysql-user=root --mysql-password=ikograce11 --mysql-table-engine=innodb cleanup

done
