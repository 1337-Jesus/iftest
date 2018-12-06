#!/usr/bin/env python3
import sys
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("-i",help="Bla",action="store_true")
parser.add_argument("-p",help="Bla",action="store_true")
parser.add_argument("-a",help="Bla",action="store_true")
args = vars(parser.parse_args())
 
if args['i']:
                while True:
                                               irule = input('1 fur HSTS, 2 für HTTP_Redirect, 3 für HEADER_Injcetion, oder exit um zu beenden ')
                                               if irule == '1':
                                                               print('config für HSTS')
                                               elif irule == '2':
                                                               print('config für HTTP_Redirect')
                                               elif irule == '3':
                                                               print('config für HEADER_Injection')
                                               elif irule.upper() == 'EXIT':
                                                               break
                                               else:
                                                               print('Option not possible!')
                                                               continue
 
if args['p']:
                while True:
                               pers_mode = input('1 fur static, 2 für dynamic: ' )
                               if pers_mode == '1':
                                               print('config für static')
                                               break
                               elif pers_mode == '2':
                                               print('config für dynamic')
                                               break
                               elif pers_mode.upper() == 'EXIT':
                                               break
                               else:
                                               print('Option not possible!')
                                               continue
 
if args['a']:
                print('atom wurde gewaehlt')

