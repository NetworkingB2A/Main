What is VIM?
Successor of VI or aka VI improved
Vim is a command line text editor that is in most linux os's.

What are the VIM modes
- while vim is open type in  :h vim-modes  to view the different vim modes.
- There are 7 basic vim modes
  - normal mode << need to know
    - default starting mode
    - access this mode from other modes by pressing ESC
    - read the file
    - accepts "invisible" commands
    - Nothing shows up at the bottom of the screen in this mode
  - visual mode << need to know
    - Enter visual mode with v from normal mode
    - apply commands on the selections of text
    - similar to clicking and dragging with a mouse to hight text
    - ESC to normal mode
    - You will see -- Visual -- at the bottom of the screen when you are in this mode.
  - select mode 
  - insert mode << need to know
    - From normal mode you press "i" to get into insert mode
    - This where text is edited normally
    - ESC to normal mode
    - You will see -- INSERT -- at the bottom of the screen when you are in this mode.
  - command-line mode << need to know
    - Enter command-line mode with : from normal mode
      - : {followed by text }
    - Modify settings, save or quit the file
    - Features such as search and replace or help menu
    - ESC to normal mode
    - You will see : at the bottom of the screen when you are in this mode.
  - ex mode
  - terminal-job mode

Save a file
- :w
- :w newfilename
  - Makes a copy of the file

Close a file
- :q (quit)
- :wq (save and quit)
- :q! (force quit)
- ZZ (save if changed and quit)