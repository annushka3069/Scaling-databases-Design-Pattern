
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
    # print 'connection from: ' + str(addr)

    while True:
        data = c.recv(2048)  # Max bytes
        if not data:
            break
        print 'from connected user: ' + str(data)
        data = str(data)
        type, command = parse_data(data)
      

        if type == 'INSERT':
             hit_master(data)
         else:
           proxy_pattern(command)
    c.close()


def parse_data(data):
    """Function that takes the data and parses it."""
    type,command = map(str.strip, data.split(',', 1))
    # TO DO ...
    # Implement a function that parses the data and detects type of command
    return type, command

def hit_master(data):
        myDB = MySQLdb.connect(host="172.31.14.98",port=3306,user="ubuntu",passwd="",db="cluster_Test")
        cHandler = myDB.cursor()
        values =str(data.split(","))

        cHandler.execute("INSERT INTO DATADUMP VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",values)
        #cHandler.execute("SHOW TABLES")
        #results = cHandler.fetchall()
        # print items[0]
        #query = "INSERT INTO DATADUMP (member_id) VALUES %s"
        #cHandler.execute("INSERT INTO DATADUMP (country) VALUES (%s)",tab[2])
        #cHandler.execute("""INSERT INTO DATADUMP (member_id) VALUES %s""", 123456)
        for r in values:
          print r

def proxy_pattern():
    # Proxy pattern
        myDB = MySQLdb.connect(host="172.31.2.100",port=3306,user="ubuntu",passwd="",db="cluster_Test")
        cHandler = myDB.cursor()
        values =str(data.split(","))

        cHandler.execute("SELECT * FROM DATADUMP")
        results = cHandler.fetchall()
        print items[0]
        #query = "INSERT INTO DATADUMP (member_id) VALUES %s"
        #cHandler.execute("INSERT INTO DATADUMP (country) VALUES (%s)",tab[2])q
        #cHandler.execute("""INSERT INTO DATADUMP (member_id) VALUES %s""", 123456)


if __name__ == '__main__':
    main()

