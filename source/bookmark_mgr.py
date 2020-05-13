#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:14:11 2019

@author: opujo
"""
# standard library imports
import datetime
import json
import logging
import re
import tkinter as tk
from tkinter import ttk, filedialog

# 3rd party impports
import requests

# internal app imports


###############################################################################
class MenuFile:
    def __init__(self, parent):
        self.master = parent
        self.create_menu()
        self.create_bindings()


    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.add_cascade(menu=self.menu, label='File')
        self.menu.add_command(label='New file', accelerator="Ctrl+N", command=self.menu_newfile)
        self.menu.add_command(label='Open file', accelerator="Ctrl+O", command=self.menu_openfile)
        self.menu.add_command(label='Save', command=self.menu_savefile)
        self.menu.add_command(label='Save as...', command=self.menu_savefileas)
        self.menu.add_separator()
        self.menu.add_command(label='Quit', command=self.menu_quit)

    def create_bindings(self):
        root.bind_all('<Control-n>', self.menu_newfile)
        root.bind_all('<Control-o>', self.menu_openfile)


    def menu_newfile(self, ev=None):
        pass


    def menu_openfile(self, ev=None):        
        filename = filedialog.askopenfilename()

        if len(filename) == 0:
            return

        # TODO read data from file


    def menu_savefile(self):
        filename = filedialog.asksaveasfilename()

        if len(filename) == 0:
            return

        # TODO save data to file


    def menu_savefileas(self):
        pass


    def menu_quit(self):
        root.destroy()


###############################################################################
class MenuManage:
    def __init__(self, parent):
        self.master = parent
        self.create_menu()
        self.create_bindings()


    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.add_cascade(menu=self.menu, label='Manage')
        self.menu.add_command(label='Sync with Pinboard', command=self.menu_sync_pinboard)
        self.menu.add_command(label='New bookmark', command=self.menu_ceate_new)
        self.menu.add_command(label='Delete bookmark', command=self.menu_delete_bookmark)
        self.menu.add_separator()
        self.menu.add_command(label='Rename tag', command=self.menu_rename_tag)
        self.menu.add_command(label='Delete tag', command=self.menu_delete_tag)
    
    
    def create_bindings(self):
        pass
    
    
    def menu_sync_pinboard(self):
        pass


    def menu_ceate_new(self):
        pass


    def menu_delete_bookmark(self):
        pass


    def menu_rename_tag(self):
        pass


    def menu_delete_tag(self):
        pass



###############################################################################
class MenuHelp:
    def __init__(self, parent):
        self.master = parent
        self.create_menu()
        self.create_bindings()


    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.add_cascade(menu=self.menu, label='Help')
        self.menu.add_command(label='Help', accelerator="F1", command=self.menu_manual)
        self.menu.add_separator()
        self.menu.add_command(label='About', command=self.menu_about)
            
    
    def create_bindings(self):
        root.bind_all('<F1>', self.menu_manual)
    
    
    def menu_manual(self, ev=None):
        pass


    def menu_about(self):
        pass



###############################################################################
class Toolbar:
    def __init__(self, parent):
        self.master = parent
        self.icon_img = {}
        self.icon_btn = {}
        self.create_bar()

    def create_bar(self):
        self.icon_img['new'] = tk.PhotoImage(file='icons/new_file.png')
        self.icon_btn['new'] = ttk.Button(self.master, image=self.icon_img['new'],
                     command=menu_file.menu_newfile)
        self.icon_btn['new'].pack(side=tk.LEFT)
        self.icon_btn['new'].bind("<Enter>", lambda e: status_msg.set_status('New file'))
        self.icon_btn['new'].bind("<Leave>", lambda e: status_msg.clear_status())

        self.icon_img['open'] = tk.PhotoImage(file='icons/open_file.png')
        self.icon_btn['open'] = ttk.Button(self.master, image=self.icon_img['open'],
                     command=menu_file.menu_openfile)
        self.icon_btn['open'].pack(side=tk.LEFT)
        self.icon_btn['open'].bind("<Enter>", lambda e: status_msg.set_status('Open a file'))
        self.icon_btn['open'].bind("<Leave>", lambda e: status_msg.clear_status())

        self.icon_img['save'] = tk.PhotoImage(file='icons/save_file.png')
        self.icon_btn['save'] = ttk.Button(self.master, image=self.icon_img['save'],
                     command=menu_file.menu_savefile)
        self.icon_btn['save'].pack(side=tk.LEFT)
        self.icon_btn['save'].bind("<Enter>", lambda e: status_msg.set_status('Save current file'))
        self.icon_btn['save'].bind("<Leave>", lambda e: status_msg.clear_status())

        self.icon_img['sep'] = tk.PhotoImage(file='icons/separator.png')
        self.icon_btn['sep'] = ttk.Label (self.master, image=self.icon_img['sep'])
        self.icon_btn['sep'].pack(side=tk.LEFT)

        self.icon_img['help'] = tk.PhotoImage(file='icons/help.png')
        self.icon_btn['help'] = ttk.Button(self.master, image=self.icon_img['help'],
                     command=menu_help.menu_manual)
        self.icon_btn['help'].pack(side=tk.LEFT)
        self.icon_btn['help'].bind("<Enter>", lambda e: status_msg.set_status('Open the help file'))
        self.icon_btn['help'].bind("<Leave>", lambda e: status_msg.clear_status())
               

###############################################################################
class StatusBar:
    def __init__(self, parent):
        self.master = parent
        self.statusbar_var = tk.StringVar(value='')
        self.start = datetime.datetime.now()
        ttk.Label(self.master, textvariable=self.statusbar_var).pack(side=tk.LEFT)
        self.check_status()

    def set_status(self, msg):
        self.start = datetime.datetime.now()
        self.statusbar_var.set(msg)

    def clear_status(self):
        self.start = datetime.datetime.now()
        self.statusbar_var.set('')

    def check_status(self, interval=10):
        now = datetime.datetime.now()
        if now - self.start >= datetime.timedelta(seconds=interval):
            self.clear_status()
        self.master.after(100*interval, self.check_status)


###############################################################################
class ListOfBookmarksPane:
    columns = {'#0': {'header': 'Id', 'width': 80 },
               'title': {'header': 'Title', 'width': 300 },
               'url': {'header': 'Url', 'width': 300 },
               'tags': {'header': 'Tags', 'width': 150 },
               'date': {'header': 'Created', 'width': 150 },
               }
    
    def __init__(self, parent):
        self.master = parent
        self.create_tree_structure()
        self.current_index = None

    def create_tree_structure(self):
        """Initialize the structure of the list, scrollbars and bindings"""
        self.tree = ttk.Treeview(self.master)
        self.tree.grid(column=0, row=0, sticky='news')
        self.tree["columns"] = tuple(self.columns.keys())[1:]
        for column in self.columns:
            self.tree.column(column, width=self.columns[column]['width'])
            self.tree.heading(column, text=self.columns[column]['header'])
        
        s_vert_tree = ttk.Scrollbar(self.master, orient='vertical', 
                                    command=self.tree.yview)
        s_vert_tree.grid(column=1, row=0, sticky='ns')
        self.tree['yscrollcommand'] = s_vert_tree.set

        s_hor_tree = ttk.Scrollbar(self.master, orient='horizontal', 
                                   command=self.tree.xview)
        s_hor_tree.grid(column=0, row=1, sticky='ew')
        self.tree['xscrollcommand'] = s_hor_tree.set

        self.tree.bind('<<TreeviewSelect>>', self.select_item)


    def rebuild_tree(self):
        """Re-writes the list, to reflect new values"""
        # remove previous list
        self.tree.delete(*self.tree.get_children())
        
        # read list of records(e.g. entries in the bibliography)
        for bookmark in database.bookmarks:
            if not self._validate_filter(bookmark):
                continue
            ident = bookmark['id']
            values = list()
            for column in self.columns:
                if column == '#0':
                    continue
                if column == 'tags':
                    values.append(" ".join(bookmark[column]))
                else:
                    values.append(bookmark[column])
            self.tree.insert('', 'end', text=ident, values=values)


    def select_item(self, *args):
        """based on the selected item, populate the detail pane"""
        self.current_id = self.tree.item(self.tree.focus(), "text")
        details_window.print_values(database.get_by_id(self.current_id))
    
    
    def _validate_filter(self, bookmark):
        """validate if bookmark is selected by filt. Return the result"""
        filt_in, filt_out = filter_window.filter
        for key, value in filt_in.items():
            if key == 'date':
                if not (value['from'] < bookmark['date'] < value['to']):
                    return False
            elif key in ['shared', 'toread']:
                if value != bookmark[key]:
                    return False
            else:
                for item in value:
                    if item not in bookmark[key]:
                        return False
        
        for key, value in filt_out.items():
            if key in ['shared', 'toread']:
                if value == bookmark[key]:
                    return False
            else:
                for item in value:
                    if item in bookmark[key]:
                        return False
        
        return True
        



###############################################################################
class DetailsPane:
    def __init__(self, parent):
        self.master = parent
        self.entries = dict()
        self.entries_var = dict()        
        self.create_structure()
        
    
    def create_structure(self):
        """Initialize the structure of the pane"""
        frame = ttk.Labelframe(self.master, text='Details pane')
        frame.grid(column=0, row=0, sticky='news')
        frame.columnconfigure(1, weight=1)
                
        for i, field in enumerate(BookmarkDatabase.bookmark_fields):
            label = ttk.Label(frame, text=field.capitalize())
            label.grid(column=0, row=i, sticky='ew')
            if field in ["shared", "toread"]:
                self.entries_var[field] = tk.BooleanVar()
                self.entries[field] = ttk.Checkbutton(
                    frame, variable=self.entries_var[field])
            elif field in ["url", "title", "description"]:
                self.entries[field] = tk.Text(frame, width=30, height=3,
                                              font="TkDefaultFont", wrap='word')
            else:
                self.entries[field] = tk.Text(frame, width=30, height=1,
                                              font="TkDefaultFont")
            self.entries[field].grid(column=1, row=i, sticky='news',
                                     columnspan=2)
            if field in ["id", "status"]:
                self.entries[field]['font'] = 'TkDefaultFont 10 italic'
                self.entries[field]['foreground'] = 'gray60'
        
        
        for child in frame.winfo_children():
            if child.winfo_class() not in ('Menu', 'TScrollbar'):
              child.grid_configure(padx=5, pady=3)

        reset_btn = ttk.Button(frame, text='Reset values', padding=3,
                                command=self._reset_button)
        apply_btn = ttk.Button(frame, text='Apply changes', padding=3,
                                command=self._apply_button)       
        del_btn = ttk.Button(frame, text='Delete', padding=3,
                                command=self._del_button)
        reset_btn.grid(column=0, row=i+1, padx=5, pady=20)
        apply_btn.grid(column=1, row=i+1, padx=5, pady=20)
        del_btn.grid(column=2, row=i+1, padx=5, pady=20)


    def print_values(self, bookmark:dict):
        if not bookmark:
            for field in BookmarkDatabase.bookmark_fields:
                if field in ["shared", "toread"]:
                    self.entries_var[field].set(False)
                else:
                    self.entries[field].replace('1.0', 'end', "")
        else:
            for field in bookmark:
                if field in ["shared", "toread"]:
                    self.entries_var[field].set(bookmark[field])
                elif field == 'tags':
                    self.entries[field].replace('1.0', 'end', 
                                                " ".join(bookmark[field]))
                elif field == 'date':
                    self.entries[field].replace('1.0', 'end', 
                                                bookmark[field].isoformat())
                else:
                    self.entries[field].replace('1.0', 'end', bookmark[field])
        
            
    def _apply_button(self):
        b = database.get_by_id(bookmark_list_window.current_id)
        for field in b:
            if field == 'id':
                continue
            elif field in ["shared", "toread"]:
                b[field] = self.entries_var[field].get()
            elif field == 'tags':
                value = self.entries[field].get('1.0', 'end')[:-1]
                b[field] = set(value.split())
            elif field == 'date':
                try:
                    b[field] = datetime.datetime.fromisoformat(
                        self.entries[field].get('1.0', 'end')[:-1])
                except:
                    status_msg.set_status("Date ISO format incorrect. Keeping previous date")
            else:
                b[field] = self.entries[field].get('1.0', 'end')[:-1]
 
        b['status'] = 'update'
        self.print_values(None)
        bookmark_list_window.rebuild_tree()
        
    
    def _reset_button(self):
        b = database.get_by_id(bookmark_list_window.current_id)
        self.print_values(b)
    

    def _del_button(self):
        b = database.get_by_id(bookmark_list_window.current_id)
        b['status'] = 'delete'
        self.print_values(None)
        bookmark_list_window.rebuild_tree()

    
###############################################################################
class FilterPane:
    def __init__(self, parent):
        self.master = parent
        self.regex = tk.BooleanVar(False)
        self.create_structure()
        self.filter = [{}, {'status': ['delete']}]
        
    
    def create_structure(self):
        """Initialize the structure of pane"""
        frame = ttk.Labelframe(self.master, text='Filter pane')
        frame.grid(column=0, row=0, sticky='news')
        frame.columnconfigure(1, weight=1)
        
        self.search_entry = tk.Text(frame, width=30, height=5,
                                        font="TkDefaultFont", wrap='word')
        self.search_entry.grid(column=0, row=0, sticky='news', columnspan=3,
                               padx=5, pady=3)
    
        regex_entry = ttk.Checkbutton(frame, text='Regex', variable=self.regex)

        apply_btn = ttk.Button(frame, text='Apply filter', padding=3,
                                command=self._apply_button)       
        clear_btn = ttk.Button(frame, text='Clear', padding=3,
                                command=self._clear_button)       
        regex_entry.grid(column=2, row=1,padx=5, pady=20)
        apply_btn.grid(column=1, row=1, padx=5, pady=20)
        clear_btn.grid(column=0, row=1, padx=5, pady=20)

        # TODO regex flag disabled for the moment -- WIP
        regex_entry.configure(state='disabled')


    def _clear_button(self):
        self.search_entry.delete('1.0', 'end')
        self.filter = [{}, {'status': ['delete']}]
        bookmark_list_window.rebuild_tree()


    def _apply_button(self):
        filt_in = dict()
        filt_out = dict()
        filter_string = self.search_entry.get('1.0', 'end')[:-1]
        
        # detecting generic fields
        for field in ('id', 'url', 'title', 'description', 'tags', 'status'):
            pattern = field + r'=(".+"|\S+)'
            match_list = re.findall(pattern, filter_string)
            if match_list:
                filt_in[field] = match_list
            pattern = field + r'!=(".+"|\S+)'
            match_list = re.findall(pattern, filter_string)
            if match_list:
                filt_out[field] = match_list
        
        # detecting boolean fields
        for field in ('shared', 'toread'):
            pattern = field + r'=(\w+)'
            match_list = re.findall(pattern, filter_string)
            if match_list:
                if match_list[0].lower() in ('yes', 'y', 'true'):
                    filt_in[field] = True
                elif match_list[0].lower() in ('no', 'n', 'false'):
                    filt_in[field] = False
            
        pattern = r'date(<|>)([:\dT-]+)'
        match_list = re.findall(pattern, filter_string)
        if match_list:
            filt_in['date'] = {'from': datetime.datetime(1970, 1, 1),
                               'to': datetime.datetime.now()}
            for match in match_list:
                if match[0] == '<':
                    filt_in['date']['to'] = datetime.datetime.fromisoformat(match[1])
                else:
                    filt_in['date']['from'] = datetime.datetime.fromisoformat(match[1])
        
        self.filter = [filt_in, filt_out]
        logging.debug(f"Search filter = {self.filter}")
        bookmark_list_window.rebuild_tree()
        
    
###############################################################################
class Pinboard:
    """
    Define all methods to access pinboard. Define the basic url,
    as well as all the different commands and information that can be
    retrieved or posted to pinboard. Using key for authentication, the
    file holding the key needs to be provided as input.
    
    Atributes:
        base_url: to access pinboard site
        command: dictionary of commands, each key will contain the path for 
            that command
        common_filters: filters to be applied always. These are applied on top
            of any filter for each request
    
    Methods:
        get_bookmarks: return all bookmarks from pinboard
        add_bookmark: add new/existing bookmark to pinboard
        delete_bookmark: delete a bookmark from pinboard
    """
    
    base_url = 'https://api.pinboard.in/v1/'
    command = {
        'get': 'posts/all',
        'add': 'posts/add',
        'delete': 'posts/delete',
        # 'get_url': 'posts/get',
        # 'recent': 'posts/recent', 
        # 'last': 'posts/update',
        # 'get_tags': 'tags/get',
        # 'delete_tags': 'tags/delete',
        # 'rename_tags': 'tags/rename',
        }
    
    def __init__(self, key_file):
        self.base_url = 'https://api.pinboard.in/v1/'

        with open(key_file) as f:
            KEY=f.readline()[:-1]
        
        self.common_filters = {'format': 'json', 
                               'auth_token': KEY}
    
        
    def get_bookmarks(self):
        """get all bookmarks from pinboard, and add them into bookmark,
        transforming to standard bookmark structure. Returns the bookmarks
        list if no error, False if any error.
        """
        # req = requests.get(self.base_url+self.command['get'], 
        #                     self.common_filters)
        
        # if req.status_code != 200:
        #     return False
        # bookmarks = json.loads(req.text)
        
        with open('../assets/my_bookmarks/all.json') as f:
            raw_list = f.read()
        
        bookmarks = json.loads(raw_list)
        
        # change formats, remove unneded fields, add fields required
        count = 0
        for b in bookmarks:
            self._format_from_pinboard(b)
            count += 1
            b['id'] = f'bk{count:05d}'        
        return bookmarks
    

    def add_bookmark(self, bookmark):
        """add a bookmark on pinboard. Return status of request."""
        self._format_to_pinboard(bookmark)
        bookmark['replace'] = 'yes'
        
        req = requests.get(self.base_url+self.command['add'], 
                           {**bookmark, **self.common_filters})
        
        return req.status_code


    def delete_bookmark(self, url):
        """delete a bookmark from pinboard. Return status of request."""
        params = {'url': url}
        
        req = requests.get(self.base_url+self.command['delete'], 
                           {**params, **self.common_filters})
        
        return req.status_code
    

    def _format_to_pinboard(self, bookmark):
        """gets a bookmark with standard definition and changes it to match
        pinboard spec
        """
        logging.debug(f'Bookmark before changing: {bookmark}')
        # renaming
        bookmark['extended'] = bookmark.pop('description')
        bookmark['description'] = bookmark.pop('title')
        bookmark['dt'] = bookmark.pop('date')
                
        # change format
        bookmark['dt'] = bookmark['dt'].isoformat(timespec='seconds') + "Z"
        bookmark['shared'] = 'yes' if bookmark['shared'] else 'no'
        bookmark['toread'] = 'yes' if bookmark['toread'] else 'no'
        bookmark['tags'] = ' '.join(bookmark['tags'])
        
        # removing
        bookmark.pop('id')
        bookmark.pop('status')
        
        # eliminating empty fields
        for field in ['extended', 'tags']:
            if not bookmark[field]:
                bookmark.pop(field) 
        
        logging.debug(f'Bookmark after changing: {bookmark}')
        
        


    def _format_from_pinboard(self, bookmark:dict):
        """gets a pinboard-like bookmark, and changes it to match the standard
        bookmark definition
        """
        # renaming
        bookmark['url'] = bookmark.pop('href')
        bookmark['title'] = bookmark.pop('description')
        bookmark['description'] = bookmark.pop('extended')
        bookmark['date'] = bookmark.pop('time')
        
        # change format
        bookmark['date'] = datetime.datetime.fromisoformat(bookmark['date'][:-1])
        bookmark['shared'] = True if bookmark['shared']=='yes' else False
        bookmark['toread'] = True if bookmark['toread']=='yes' else False
        bookmark['tags'] = set(bookmark['tags'].split())
        
        # new fields
        bookmark['id'] = '' # id needs to be generated at the database level
        bookmark['status'] = 'synced'
        
        # removing
        bookmark.pop('hash')
        bookmark.pop('meta')
        
    
    def _web_request(self, command:str, params:dict):
        pass
        


###############################################################################
class BookmarkDatabase:
    """
    Holds the structure of the database of bookarks. This database contains
    some basic fields (e.g. last update, etc.), and the list of bookmarks.
    This class has functions to update the database. 
    
    Attributes (fields):
        sycned: to express whether it's synced or not with the web
        bookmarks: list of bookmarks
    
    Methods:
        add_bookmark: to add a new boomark
        update_bookmark: make changes to an existing bookmark
        delete_bookmark: to delete an existing bookmark
        update_from_pinboard: get new bookmark list from pinboard        
    """
    bookmark_fields = ['id', 'url', 'title', 'description', 'tags', 'date', 
                       'shared', 'toread', 'status']
    
    def __init__(self):
        self.bookmarks = list()
        self.synced = False
    
    def add_bookmark(self, url, title, description='', tags=set(), 
                     shared=False, toread=False):
        """add new bookmark to the database"""
        bookmark = dict()
        bookmark['id'] = self._generate_id()
        bookmark['url'] = url
        bookmark['title'] = title
        bookmark['description'] = description
        bookmark['tags'] = tags
        bookmark['shared'] = shared
        bookmark['toread'] = toread
        bookmark['status'] = 'update'
        bookmark['date'] = datetime.datetime.utcnow()
        self.bookmarks.append(bookmark)
        self.synced = False
        
    
    def update_bookmark(self, ident, **kwargs):
        """update an existing bookmark with some fields changed"""
        for b in self.bookmarks:
            if b['id'] != ident:
                continue
            for param in kwargs:
                if param in self.bookmark_fields:
                    b[param] = kwargs[param]
            break
        
        self.synced = False
    
    
    def delete_bookmark(self, ident, **kwargs):
        """mark a bookmark to be deleted. It will be actually deleted after
        a synchronisation with pinboard, this is to ensure we know what 
        bookmarks to delete in pinboard
        """
        for b in self.bookmarks:
            if b['id'] != ident:
                continue
            b['status'] = 'delete'
            break
        
        self.synced = False
        
    
    def update_from_pinboard(self, pin:Pinboard):
        """create new database from info in pinboard"""
        self.bookmarks = pin.get_bookmarks()
        if self.bookmarks:
            self.synced = True
            error = True
        else:
            self.bookmarks = list()
            error = False
            
        return not error    # functions return True in case of no error
    
    
    def update_to_pinboard(self, pin:Pinboard):
        """update current database to pinboard. Only the changes"""
        error = False
        for b in self.bookmarks:
            if b['status']:
                if b['status'] == 'delete':
                    resp = pin.delete_bookmark(b['url'])
                    if resp == 200:
                        self.bookmarks.remove(b)
                    else:
                        error = True
                    
                elif b['status'] == 'update':
                    resp = pin.add_bookmark(b)
                    if resp == 200:
                        b['update'] = None
                    else:
                        error = True
        
        if not error:
            self.synced = True
        
        return not error    # functions return True in case of no error


    def get_pos_by_id(self, identifier):
        """return the position of bookmark identifier in the list"""
        for i, b in enumerate(self.bookmarks):
            if b['id'] == identifier:
                return i
        return None
    
    
    def get_by_id(self, identifier):
        """return the bookmark with identifier as id"""
        for b in self.bookmarks:
            if b['id'] == identifier:
                return b
        return None
    
    
    def _generate_id(self):
        """return a new id, different from all in database"""
        highest = 0
        for b in self.bookmarks:
            highest = max(highest, int(b['id'][2:]))
        highest += 1
        return f'bk{highest:05d}'




# TODO create main function
###############################################################################
###############################################################################
###############################################################################
def main():
    global root, menu_file, menu_manage, menu_help, status_msg, database
    global details_window, bookmark_list_window, filter_window
    
    logging.basicConfig(level=logging.DEBUG, 
                        format=' %(asctime)s - %(levelname)s - %(message)s')
    
    
    # setting up the main frames of the window, and title
    # TODO move this code to a separate function
    root=tk.Tk()
    root.title("bookmark-mgr")
    # root.iconbitmap(root,default='icons/clienticon.ico')
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icons/clienticon.png'))
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    
    toolbar = ttk.Frame(root, relief='raised', padding=2)
    toolbar.grid(column=0, row=0, columnspan=2, sticky='ew')
    toolbar.columnconfigure(0, weight=1)
    
    listframe = ttk.Frame(root, padding=10)
    listframe.grid(column=0, row=1, rowspan=2, sticky='news')
    listframe.columnconfigure(0, weight=1)
    listframe.rowconfigure(0, weight=1)
    
    filterframe = ttk.Frame(root, padding=10)
    filterframe.grid(column=1, row=1, sticky='news')
    filterframe.columnconfigure(0, weight=1)
    filterframe.rowconfigure(0, weight=1)
    
    propframe = ttk.Frame(root, padding=10)
    propframe.grid(column=1, row=2, sticky='news')
    propframe.columnconfigure(0, weight=1)
    propframe.rowconfigure(0, weight=1)
    
    statusbar = ttk.Frame(root, relief='sunken', padding=2)
    statusbar.grid(column=0, row=3, columnspan=2, sticky='ew')
    statusbar.columnconfigure(0, weight=1)
    
    
    ######################### Menús and toolbar commands #########################
    
    root.option_add('*tearOff', tk.FALSE)
    menubar = tk.Menu(root)
    root['menu'] = menubar
    menu_file = MenuFile(menubar)
    menu_manage = MenuManage (menubar)
    menu_help = MenuHelp (menubar)
    toolbar_buttons = Toolbar (toolbar)
    
    ######################## Other frames ########################

    filter_window = FilterPane(filterframe)
    bookmark_list_window = ListOfBookmarksPane(listframe)
    status_msg = StatusBar(statusbar)    
    pin = Pinboard('pinboard.key')
    database = BookmarkDatabase()
    database.update_from_pinboard(pin)
    bookmark_list_window.rebuild_tree()
    details_window = DetailsPane(propframe)
    
    
    root.mainloop()

if __name__ == "__main__":
    main()