#!/usr/bin/env python3

import sys


if '-p' in sys.argv:
    print('persitance wurde gewaehlt, wähle mode 1 oder 2')
    pers_mode = input('1 fur static, 2 für dynami:' )
    if pers_mode == 1:
        print('config für static')
    elif pers_mode == 2:
        print('config für dynamic')

if '-i' in sys.argv:
    print('irule wurde gewaehlt')
    irule = 0
    while irule != 'exit':
        irule = input('1 fur HSTS, 2 für HTTP_Redirect, 3 für HEADER_Injcetion, oder exit um zu beenden' )
        if irule == 1:
            print('config für HSTS')
        elif irule == 2:
            print('config für HTTP_Redirect')
        elif irule == 3:
            print('config für HEADER_Injection')

if '-a' in sys.argv:
    print('atom wurde gewaehlt')

