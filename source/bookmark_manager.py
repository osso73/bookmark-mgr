# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:14:11 2019

@author: opujo
"""

import urllib.request
import urllib.parse
import json

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Pinboard:
    """
    Defines all methods to access pinboard. Defines the basic url,
    as well as all the different commands and information that can be
    retrieved or posted to pinboard. Using key for authentication, the
    file holding the key needs to be provided as input.
    
    Fields:
        base_url: to access pinboard site
        KEY: authentication key to access pinboard. Retrieved from a local file
        command: dictionary of commands, each key will contain the path for 
            that command
        common_filters: filters to be applied always. These are applied on top
            of any filter
    
    Methods:
        create_url (internal??): will build the url from the different components. 
            Accepts command and a list of additional filters.
        ...tbd...
    """
    def __init__(self, key_file):
        """starts all variables, and gets the key from the file passed as parameter"""
        self.base_url = 'https://api.pinboard.in/v1/'
        self.command = { # list of commands that I'll be using
                'get': 'posts/all',
                'add': 'posts/add',
                'delete': 'posts/delete',
                'get_url': 'posts/get',
                'recent': 'posts/recent', 
                'last': 'posts/update',
                'get_tags': 'tags/get',
                'delete_tags': 'tags/delete',
                'rename_tags': 'tags/rename',
                }
        self.common_filters = ['format=json']
        with open(key_file) as f:
            self.KEY=f.readline()
    
    def create_url(self, cmd, filt=list()):
        """return url using the cmd and filters passed, adding the base_url and KEY"""
        url = "{}{}?auth_token={}".format (self.base_url, self.command[cmd], self.KEY)
        url = "&".join([url]+self.common_filters+filt)
        
        return url
    
    
class Bookmark:
    """
    Defines structure of a bookmark, with all the fields.
    Includes functions to compare bookmarks, comparison is based on dates
    (should allow to compare with a date as well).
    
    Each bookmark has the following fields:
       url: url of the bookmark
       title: title or short description
       description: extended description about the bookmark
       time: time when it was created for the first time
       private: is this privae (or not, i.e. public) bookmark
       to_read: is this a to_read tag or not?
       tags: list of tags
    """
    pass


class Bookark_db:
    """
    Holds the structure of the database of bookarks. This database contains
    some basic fields (e.g. last update, etc.), and the list of bookarks.
    This class has functions to update the database, and also download/upload 
    from pinboard.in website. 
    
    Fields:
        web_update: timestamp of last update from the web
        status: to express whether it's synced or not with the web
        bookmarks: list of bookmarks
    
    Methods:
        get_update: to get info from the web
        
    """
    pass



root=tk.Tk()

pin = Pinboard('pinboard.key')

for n in pin.command:
    print ("{} - {} --> {}".format(n, command[n], pin.create_url(n, ['tag=hot'])))
    

############################ Menús and toolbar commands ############################

root.option_add('*tearOff', tk.FALSE)
menubar = tk.Menu(root)
root['menu'] = menubar

"""
menu_file = MenuFile(menubar)
menu_edit = MenuEdit (menubar)
menu_bibtex = MenuBibTeX (menubar)
menu_help = MenuHelp (menubar)

toolbar_buttons = Toolbar (toolbar)
"""


root.mainloop()
