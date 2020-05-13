# bookmark-mgr

Simple program in python+tkinter to manage your bookmarks from [pinboard][pinboard_lnk].

## Objective

The reason why I started this project is to practice with python and tkinter, making use of a public API such as pinboard. Besides that, I always find, in general in any service, the use of tags for filtering the results is very poor: it is often difficult to filter using several tags, and almost impossible to use the NOT tag (as in: show me elements that have the tag *python* but don't have *tkinter*). So my intention here is to develop a search functionality allowing this more powerful search, similar to the syntaxis used by google when searching emails in gmail, for example.

So the idea is to use this program to download your bookmarks from pinboard, manage and edit them locally more easily, and then synchronize these changes with [pinboard][pinboard_lnk]. A copy of the bookmarks is kept locally, so you only synchronize the changes since the last connection.

## Usage

For the moment the program is not working yet, still being built. But note that you will need to have a pinboard account and an API Token in order to test functionality with pinboard. Put your API token in a text file in the same folder as the main program.


## Contribution

I would appreciate any feedback regarding my code, notice I'm still quite new to Python. So please bare with me regarding any mistakes in terms of use of language, formatting, best practices, etc.

In case you want to contribute, you are more than welcome, although this is not the primary objective of this repository. Drop me a note.


## License

This project is licensed under [the MIT license](https://tldrlegal.com/license/mit-license).


[pinboard_lnk]: https://pinboard.in
