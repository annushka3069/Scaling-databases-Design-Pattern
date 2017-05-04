
#!/usr/bin/python
"""Python module that receives TCP requests."""

import socket
import MySQLdb


host = '172.31.19.224'
port = 5001


def main():
    """Main."""
    s = socket.socket()
    s.bind((host, port))

    s.listen(1)  # Listen to one connection
    c, addr = s.accept()
    print 'connection from: ' + str(addr)

    while True:
        data = c.recv(2048)  # Max bytes
        if not data:
            break
        print 'from connected user: ' + str(data)
        data = str(data)

        # TO DO ...

        # Implement a function that parses received data

        type, command = parse_data(data)
        # We need to detect INSERT or SELECT
        # In case of "INSERT", we hit Master node in MySQL Cluster
        # In case of "SELECT", we call the

        if type == 'INSERT':
             hit_master(data)
        # else:
        #   my_pattern(command)
        #

    # c.close()


def parse_data(data):
    """Function that takes the data and parses it."""
    type,command = map(str.strip, data.split(',', 1))
    # TO DO ...
    # Implement a function that parses the data and detects type of command
    return type, command

def hit_master(data):
        myDB = MySQLdb.connect(host="172.31.14.98",port=3306,user="ubuntu",passwd="",db="cluster_Test")
        cHandler = myDB.cursor()
        cHandler.execute("INSERT INTO DATADUMP values "+str(data.split(",",1))+", "+str(data.split(",",2))+", "+str(data.split(",",3))+", "+str(data.split(",",4))+", "+str(data.split(",",5))+", "+str(data.split(",",6))+", "+str(data.split(",",7))+", "+str(data.split(",",8))+", "+str(data.split(",",9))+", "+str(data.split(",",10)) )

def my_pattern():
    """Implement algorithm of the pattern here."""
    # Connect to MySQL Cluster
-- INSERT --                                    