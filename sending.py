#!/usr/bin/python
"""Python module that sends TCP requests to AWS instance."""

import socket
import time


host = '172.31.19.224'
port = 5001

# TO DO ...
# Add either "INSERT" OR "SELECT" strings to the data being sent

type = 'INSERT,'


def main():
    """Main."""
    s = socket.socket()
    s.connect((host, port))

    with open('data_dump.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            # s.send(line)
            data = type + str(line)
            # data = s.recv(1024)
            # print 'Sending data: ' + str(data)
            s.send(data)
            print str(data.split(',', 10 ))
            time.sleep(0.1)

    s.close()


if __name__ == '__main__':
    main()

