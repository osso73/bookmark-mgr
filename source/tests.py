#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:50:41 2020

tests.py - Execute tests to validate functionality of bookmark-mgr main
program

--------------- TO BE UPDATED USING unitest MODULE ---------------

@author: opujo
"""

# standard library imports
import logging
import datetime

# 3rd party impports

# internal app imports
from bookmark_mgr import Pinboard, BookmarkDatabase




######################## TESTS ##################################
def check_download_bookmarks():
    """checks that bookmarks are downloaded from pinboard correctly"""
    pin = Pinboard('pinboard.key')
    
    bookmarks = pin.get_bookmarks()
    
    if not bookmarks:
        print("There was an error, I could not retrieve info from pinboard.")
    else:
        for b in bookmarks:
            for key, val in b.items():
                print(f'{key}: {val}')
            print('-'*25)


def upload_new_bookmark():
    """checks that bookmarks are downloaded from pinboard correctly"""
    pin = Pinboard('pinboard.key')
    bookmark = {'id':'bk00023', 
                'url':'http://www.example.com', 
                'title': 'This is an example of bookmark',
                'description': '',
                'tags': set(),
                'shared': True,
                'toread': False,
                'status': 'update',
                'created': datetime.datetime(2020, 5, 7, 11, 23, 55)
                }
    resp = pin.add_bookmark(bookmark)
    print("Response:", resp)


def check_bookmark_database():
    pin = Pinboard('pinboard.key')
    database = BookmarkDatabase()
    database.update_from_pinboard(pin)
    for b in database.bookmarks:
        for key, val in b.items():
            print(f'{key}: {val}')
        print('-'*25)

def check_update_bookmark():
    pin = Pinboard('pinboard.key')
    database = BookmarkDatabase()
    database.update_from_pinboard(pin)
    database.update_bookmark('bk00004', description="testing the API")
    for b in database.bookmarks:
        for key, val in b.items():
            print(f'{key}: {val}')
        print('-'*25)
    
def check_add_bookmark():
    pin = Pinboard('pinboard.key')
    database = BookmarkDatabase()
    database.update_from_pinboard(pin)
    database.add_bookmark('http://www.example.com', 'An example bookmark', 
                          description="testing the API")
    for b in database.bookmarks:
        for key, val in b.items():
            print(f'{key}: {val}')
        print('-'*25)

def check_sync_to_pinboard():
    pin = Pinboard('pinboard.key')
    database = BookmarkDatabase()
    database.update_from_pinboard(pin)
    database.update_bookmark('bk00004', description="testing the API")
    database.add_bookmark('http://www.example.com', 'An example bookmark', 
                          description="Testing new bookmark")
    print('Database status (synced):', database.synced)
    print('Uploading to pinboard...')
    database.update_to_pinboard(pin)
    print('Database status (synced):', database.synced)
    
    
def check_delete_bookmark():
    # upload_new_bookmark()
    pin = Pinboard('pinboard.key')
    resp = pin.delete_bookmark('http://www.example.com')
    print("Response:", resp)
    

def build_list():
    pin = Pinboard('pinboard.key')
    database = BookmarkDatabase()
    database.update_from_pinboard(pin)
    bk_list = ListOfBookmarks()
    bk_list.rebuild_tree(database.bookmarks)
    



ALL_TESTS = [check_download_bookmarks, check_bookmark_database, 
             check_update_bookmark, check_add_bookmark, check_sync_to_pinboard,
             upload_new_bookmark, check_delete_bookmark, build_list]

CURRENT_TESTS = [build_list]


logging.basicConfig(level=logging.DEBUG, 
                    format=' %(asctime)s - %(levelname)s - %(message)s')

for test in CURRENT_TESTS:
    test()