# Data Classes
##  What is a DataClass?
Data class is a builtin python function that will allow you to make a standard class that will take a decorator of the dataclass module.  


Really how it helps is in a normal class that you create you will need to create all the dunder magic methods and create all your attributes for you, saving you time as you create more and more classes. Looking at example code 1, you will me create a class and looking at the example return you will see the output of the class. Now look at example code 2 and using a data class you will see the amount of reduction in code.

!!! NOTE !!! 
- In these examples I am show the default dataclass. You can tell a data class not the create some of the dunders, if you want.
- One limitation( that i have seen so far, maybe I'm wrong) is that you can't create class attributes. 

Example code 1

```python

class NetworkDevice:
    def __init__(self, device_type, hostname, host_ip_address, host_username, host_password):
        self.device_type = device_type
        self.hostname = hostname
        self.host_ip_address = host_ip_address
        self.host_username = host_username
        self.host_password = host_password
    
    def __repr__(self):
        return f''' 
NetworkDevice: 
    Device Type: {self.device_type}, 
    Hostname: {self.hostname}, 
    Host IP Address: {self.host_ip_address}, 
    Host username: {self.host_username}, 
    Host Password: {self.host_password}
'''
        
    def __eq__(self):
        pass
```

Example code 2
```python
from dataclass import dataclass

@dataclass
class NetworkDevice:
    device_type: str
    host_name: str
    host_ip_address: str
    host_username: str
    host_password: str

```
Example return 2
## Gotchas
When you use a data class you do lose some of your abilities to customize.
TODO: Show some examples of features you lost by using data classes.