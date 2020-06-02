# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import os
import fileinput
import re

dir = sys.argv[-1]
opts = sys.argv[1:-1]


def read_or_create_login():
    try:
        with open(dir + '/login.conf', 'r+') as f:
            lines = f.read().splitlines()
            username = lines[0]
            password = lines[1]
            print('usernmae: ' + username + '\npassowrd: ' + password)
    except FileNotFoundError:
        print('file not found, creating login.conf')
        create_login()
    except IndexError:
        print('file is corrupt, re-creating login.conf')
        create_login()


def create_login():
    with open(dir + '/login.conf', 'w+') as f:
        print('Please enter credentails...')
        username = input('Username: ')
        f.write(username + '\n')
        password = input('Password: ')
        f.write(password)


def edit_file(path):
    for line in fileinput.input(path, inplace=True):
        #add autehntication config
        print(re.sub('^auth-user-pass.*', 'auth-user-pass login.conf', line, 1), end='')

    for line in fileinput.input(path, inplace=True):
        #delete 'comp-lzo no' to prevent deprecation warning
        print(re.sub('^comp-lzo no.*', '', line, 1), end='')

def process_files():
    with os.scandir(dir + '/') as it:
        for entry in it:
            if entry.name.endswith('ovpn') and entry.is_file():
                edit_file(dir + '/' + entry.name)

def main():
    if '-f' in opts:
        create_login()
    else:
        read_or_create_login()

    process_files()


if __name__ == "__main__":
    main()
