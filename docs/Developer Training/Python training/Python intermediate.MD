## Error Handling in Python
 I need to find better documentation than the book

## Classes
What is an object?
A object is two things
- Attributes
  - data about a object
  - Can have private or public attributes
- Methods
  - What a object can really do
  - Can have private or public methods
  - Functions created inside a class are called methods.

NOTE extra learning for classes
To learn more about classes, methods, and inheritance, you can refer to the Python documentation. https://docs.python.org/3/tutorial/classes.html
if you would to to find out more about a module or the methods use the following commands.
- help(module) or help(module.function)
- dir(module)

### Attributes
Class Attributes
- All instances of a object of the class type will receive this attribute
 example
In [1]: class Person(): 
   ...:   person_type = "Homosapien" 

adam = Person() 
adam.person_type
Out[2]: 'Homosapien'


Instance Attributes
This uses an initializer. This is unique to each object



class Person:
  person_type = "Homosapien" #this is a class attribute 
  def __init__(self, height, weight, sex):
        self.height=height #<<<< instance attribute
        self.weight=weight #<<<< instance attribute
        self.sex=sex       #<<<< instance attribute

What is a magic method?

A magic method is a special method that you can define to add 'magic' to your classes. you can add built in methods to you classes  
example  

error with no length method  
<code>
\>>> class Friends:
...     members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]
...   
\>>> my_list_friends = Friends()  
\>>> len(my_list_friends)  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'Friends' has no len()  
</code>  
no error with length method  

<code>
>>> class Friends:  
...     members=['Ross', "Phoebe",   'Chandler', 'Joey', 'Monica', "Rachel"]  
...     def __len__(self):  
...         return len(self.members)  
...

\>>> my_list_friends = Friends()  
\>>> len(my_list_friends)  
6
</code>

Here is another example. but this time I am trying to see if a name is in the list of friends  

\>>> class Friends:  
...     members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]  
...     def __len__(self):  
...         return len(self.members)  
...   
\>>> if 'adam' in my_list_friends:  
...     print ('adam is in the list')  
... else:  
...     print('adam is not a friend. :( ')  
...   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: argument of type 'Friends' is not iterable  
>>>   
KeyboardInterrupt  
>>>   

### Here is a version of the check to see if adam is a friend.  

\>>> class Friends:  
...     members=['Ross', "Phoebe", 'Chandler', 'Joey', 'Monica', "Rachel"]  
...     def __len__(self):  
...         return len(self.members)  
...     def __contains__(self, friend):  
...         return friend in self.members  
...   
\>>> if 'adam' in my_list_friends:  
...     print ('adam is in the list')  
... else:  
...     print('adam is not a friend. :( ')  
...   
adam is not a friend. :( 


You can also do a string magic method and make your class look even prettier.
class Person:
  person_type = "Homosapien" #this is a class variable 
  def __init__(self, height, weight, sex):
        self.height=height   #<<<< instance attribute
        self.weight=weight   #<<<< instance attribute
        self.sex=sex         #<<<< instance attribute
  def lb_to_kg(self):
      weight_in_kg = self.weight/2.205
      print(weight_in_kg)
  def dominate_hand(self, hand):
        if hand in ["right", "Right", "r", "R" ]:
          print("You are right handed")
        elif hand in ["left", "Left", "l", "L"]:
          print("You are left handed")
        else:
          print("You are no handed?")
  def __str__(self):
        return f"I am a person, I am { self.height } ft tall, I weigh {self.weight} lbs. I am also a {self.sex} "

\>>> adam=Person(6,250,"Male")  
\>>> print(adam)  
I am a person, I am 6 ft tall, I weigh 250 lbs. I am also a Male   


### Private Membership
With python you can only say that a attribute or method is private. you can't really block the use of the private member from public use.  
You would put an underscore in front of a private member to signify that the user of your app should not use this member. That this member should only be used for inside the app

### Property Decorator

What is a decorator in python?  
A decorator is a function in python that takes another function as its argument and returns yet another function. Decorators can be extremely useful as they allow the extension of an existing function, without the modification to the original function source code.

What is a property decorator in python?  
@property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters.  

This whole concept starts to get hard to explain without examples. see the sample code with the student class.

### Static Methods
A static method can not change the instance or the class. Its more of a function. You could create that same function outside of you class, but creating this will allow you to always have the method to use whenever you want.

### Class Methods

### Inheritance 

Best practices
- Use uppercase letters for a class name
- Use self as the first positional argument. You could use others besides self, but don't do it. just use self.

Environment variables within python
- You can create .env file and add your environmental variables there instead of putting them in a .bash file or putting them in your OS specific env files. You will need to pip install and import a module call "dotenv"