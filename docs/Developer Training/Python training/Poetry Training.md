pip install poetry
Next you need a Toml (Tom's obvious minimal language) file. In this file you will need some basics like 
- name 
- version
- description
- authors
- license
- readme
- dependencies

You can have this file created for you by using the poetry init file. it will ask you a few questions to help guide you through the creation of the toml file. 

after this file is created you can use poetry install to create the virtual environment. 

find out info about the virtual environment by using ```poetry env info```. by default the venv is created somewhere on your pc in a cache folder. this may not be what you want. You can adjust this by changing the poetry config settings. one example would be   
```poetry config virtualenvs.in-project true```

To now run code in the venv you type ```poetry shell```.

to add a package you simply type ``` poetry add request```. poetry will update your toml file for you!!! you can do the same with the remove keyword.


Private Repository Example
https://python-poetry.org/docs/repositories/#private-repository-example