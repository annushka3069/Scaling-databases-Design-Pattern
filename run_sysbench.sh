#!/bin/bash
output clear

#Connect to the remote MySQL and run sysbench
dbName=cluster_Test
user=mysql
password=''
driver=ndbcluster
host=172.31.14.98
size=300000
function TestSysbench {
	##Prepare a test table
	sysbench --test=oltp --oltp-table-size=$size --mysql-db=$dbName --db-driver=$driver --mysql-host=$host --mysql-user=$user --mysql-password=$password --mysql-table-engine=$driver prepare

	##Read-Only Test
	sysbench --test=oltp --oltp-table-size=$size --db-driver=$driver --mysql-host=$host --mysql-user=$user --mysql-password=$password --mysql-db=$dbName --db-driver=$driver --mysql-host=$host --max-time=60 --oltp-read-only=on --max-requests=0 --num-threads=8 --mysql-table-engine=$driver run

	##Mixed Test 8 threads
	sysbench --test=oltp --oltp-table-size=$size --oltp-test-mode=complex --oltp-read-only=off --num-threads=8 --max-time=60 --max-requests=0 --mysql-db=$dbName --db-driver=$driver --mysql-host=$host --mysql-user=$user --mysql-password=$password --mysql-table-engine=$driver run

	##Cleanup the test table
	sysbench --test=oltp --mysql-db=$dbName --db-driver=$driver --mysql-host=$host --mysql-user=$user --mysql-password=$password --mysql-table-engine=$driver cleanup
 }

TestSysbench
