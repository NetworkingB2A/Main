# Linux

## BASH
BASH stands for Bourne Again Shell.
BASH is one of the most popular shells available today. 
Bash supports features such as piping. variables, evaluations of conditions and iterations.

Quick linux commands  
| Command | Command name | Command description | Important Flags |
|---------|--------------|---------------------|-------|
| man { command name} | Manual | This command will provide information about another command
| cat {file name} | Concatenate |  This command will show the output of a file right on your screen. The command can also be used for outputting test to a new file.
| cd  {location to move to} | Change dictatory | This command will allow you to change your current dictatory
| pwd | Present working dictatory | This command will print out your current working dictatory to your screen. This can be helpful for scripting.
| ls |  List directory contents | This command will list out the contents of a directory | -a (Shows hidden files), -l (show file permissions)
| mkdir {new directory name} | Make directory | This is used to a new directory
| cp {copy from} {copy to} | Copy | This will copy a file or a directory | -r (copy a folder and all the files in the folder)
| mv {move from} {move to} | Move | This will move one files from a directory to a different directory. You would also use this to rename a file.
| rm {file name} | Remove | This will remove a file or a folder. | -r (removes directories and their contents), -f (this will force removal of files and never prompt)
| touch {File name} | Touch | This will create a file or update the modified date of a file.

## Environment Variables
What is an environment variable?
- Its really just a variable that you set for you OS. This can be set for anything. You can setup a folder as a variable, you can set up an API key as a variable, you can set up a number, ect. 
- You would do this in programming to set up a folder location mapped to your variable, that way you can call this variable in your OS to help you find folders better.  
- Variables are only loaded at the start of your terminal session.

Add your environment variable to your .bashrc either by
- nano into your .bashrc
- or $ echo "export PATH=$PATH:/{LOCATION NAME}" >> .bashrc

then run source ~/.bashrc
