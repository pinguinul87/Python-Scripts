#!/usr/bin/python3
#Simple port scanner based on the socket module

import time
from socket import *

startTime = time.time()

if __name__=='__main__':
    target = input('host to scan: ')
    t_IP = gethostbyname(target)
    print('starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('port %d: OPEN' % (i,))
        s.close()

print('time taken: ', time.time() - startTime)
