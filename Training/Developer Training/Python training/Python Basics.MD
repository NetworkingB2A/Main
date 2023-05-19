You can style you code with different types of standards. Two of the most popular are:
- Pep8 
- Black

The zen of python is the commandments of python. it can be accessed by typing <code> import this </code> in a python interpreter. 

### Serialization and deserialization of data
Serialization and deserialization is the idea of taking data and trasforming so tech can exchange the data better. one example from your day to day life would include a phones call. you talk a person your phone will transform or serialize your spoken words into bits that can then be passed from phone to phone. the other phone will deserialize the data, transforming it from bits back into spoken words.
In computer science one example would be take a data sctructure or objects and transforming it into an data that a programming laguage can handle better. example taking a set of JSON data and converting it dictionary and lists for python to use.

You can use  <code>  help (module-name) </code> to find out how to use a module.

If you want to avoid doing a bunch of escape characters you can us the use a raw string. 


Parts of a python program
Modules
- Modules are really just a piece code that you import into your program. everything you import is a module.
- modules contain functions, classes, global variables, ect
- Why use modules
  - Easier readability/maintainability
  - Low coupling/high cohesion
    - Modules should written in such a way that they do not have any interdependencies. 
  - Code reusability
  - Collaboration

Functions
- Fuctions are used when you find yourself using the same code over and over again. It is often a good idea to put that code into a function so you dont have to copy paste the code
Classes
- Classes is a construct that is used in OOP.
- This is generally though of a way to define and interact with an object.
- Often referred to as a blueprint

One important feature of python is that amount of built in libraries and the amount of open source libraries that have been written out in the community. To view a list of all the built-in libraries for python go to https://docs.python.org/3/library

## list methods
|Method|What it does|
|-|-|
| list.append(element) | Add an element to the end of the list |
| list.clear() | Removes everything from the list |
| list.copy() | Returns a copy of the list. This would be useful when you want to copy the list and you dont just want to create a pointer to the old list. | 
| list.count(element) | shows the number of the elements with the specified value | 
| list.extend(alist) | adds the element of a list to the end of the current list |
| list.index() | Returns the index number of the fist element with a specified value | 
| list.insert(index, element) | Adds and element at a specified index value |
| list.pop(index) | Removes an element at a specific index position, or if not index position is provided, removes the last item on the list | 
| list.remove() | Removes a list item with a  specified value | 
| list.reverse() | Reverses the list order | 
| list.sort() | sorts the list alphabetically | 

## Sets notes
What is a set?
- It is an unordered grouping of data and is defined by using the curly braces of a dictionary, without the key:value pair.
- Sets by default are mutable.
- To join two sets your would use the | (pipe), just like a math equation.
- You can find the intersections of two sites with the &.
- One advantage is that Sets logic can be performed a lot quicker than list logic can be.



## Function Notes
Basic function rules
- Must not start with a number
- Must not be a reserved Python word, or a name that has already been used as a function or variable.
- Can be any combination of A-Z, a-z, 0-9, underscore or a dash.

IMPORTANT NOTE ABOUT FUNCTIONS
- Keyword augments will help you a lot.
- if you write a basic function without keywords you will have to pass detail in a very specific order.
  - Example - def( username, first_name, last_name). 
  - If you create this as a basic and you change the order of these names when you call the function, your program will not behave how you expect it to.
- Here is why you should use keyword arguments. A keyword argument is a name/value pair that you pass to a function.
- You might not know how many arguments to expect. Python allows you to use * and ** (often referred to as *args and **kwargs) to define any number of arguments or keyword arguments.
- *args is a single argument that you pass in to your function. REMEMBER *args is still a positional argument call for your function. **kwargs is a Key value pair that you would pass into your function.
- You can define a default value argument in case you have an empty value to send to a function.
- 

<code>\_\_name__</code> Specially named variable allowing us to detect whether a module is run as a script or imported into anther module.
When you call the module while in a python interpreter, the name of the module will print out. when you call the module from a bash shell, the name \_\_main__ will print out. 

if you add the following code the your script, when you call the module from a bash shell. you will be able to define a function that you want to have run right away.

<code>if \_\_name__ == '\_\_main__';  
&nbsp;&nbsp;&nbsp;&nbsp;module_name()</code>

if you import this module into a python interpreter, python will know just to import the functions and not call any of them. if you call this module into a bash shell python will call whatever function you define in your if statement. 


Check out how to use command line arguments. 



An non empty string will always return true.
Watch out for the following. it will return true, because what you are really saying is that if apples is equal to bananas or if peach print true.
if "apples" == "bananas" or "peach"
    print("this is true")
else:
    print ("this is false")

instead do the following. 
if "apples" in ["bananas", "peach"]
    print("this is true")
else:
    print ("this is false")


## Logging
logging module built into python. No need to install anything special.

Link to the python documentation.
https://docs.python.org/3/library/logging.html


### Why use logging vs print?
Logging will allow you to capture additional data about the running of your code. It will give you flexibility as to how you capture your logs. Print only allow very basic capturing of your logging.



### logging levels
| Level | Numeric value | Description
|-|-|-|
|CRITICAL| 50| A serious error, indicating that the program itself may be unable to continue running.|
|ERROR| 40| Due to a more serious problem, the software has not been able to perform some function.|
|WARNING| 30| An indication that something unexpected happened, or indicative of some problem in the near future. |The software is still working as expected. This is the default level for the logging module.
|INFO |20| Confirmation that things are working as expected|
|DEBUG| 10| Detailed information, typically of interest only when diagnosing problems. When this is used it works a lot like the print statement and displays basic data to the screen. |
|NONSET| 0||

### More advanced logging
If you default to the root logging and you decide to import a different module that also has a root logger, the root logger of the imported class will actually do the logging and the logger you have in your main code down below will not be called, because you already have a root logger called.
Example of best practice code

using the \_\_name__ will pass the name of the module you are running into the logger, this will replace the word root in the logger.
<code>
import logging
logger = logging.getLogger(\_\_name__)

#You would use this next part if you want to customize your logger a bit more. This will allow you to change the root logger info.
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('runbook_logging/testlog2.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

</code>
You can also do a logging.exception inside a try/except block to log the traceback errors.

If you want this logging to show up on your console window you can use a stream Handler.


### Other
if you call a method without the parentheses, the code will call a memory reference to the method. 