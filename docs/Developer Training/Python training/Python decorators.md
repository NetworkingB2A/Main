## Decorator

### What is a decorator in python?  
A decorator is a function in python that takes another function as its argument and returns yet another function. Decorators can be extremely useful as they allow the extension of an existing function, without the modification to the original function source code.

### What is a property decorator in python?  
@property decorator is a built-in decorator in Python which is helpful in defining the properties effortlessly without manually calling the inbuilt function property(). Which is used to return the property attributes of a class from the stated getter, setter and deleter as parameters.

Using a property decorator will allow a person using the class to use a method to either get, set or delete an attribute. this is important because you may want to do checks against an attribute to make sure a person is using the attribute properly.

In example code 2, allow a user to see the username name, but when they try to access the password I have code that shows them * instead of the actual password.


in example code 3 I make sure a user is giving an it for the vlan number and not a string. look at @access_vlan.setter.


#### Example code 1  
In this example I will be using the default getter.
```python
class NetworkDevice:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
```
#### Example return 1
In the code above you will see that the attribute is actually set to _username. By using the 'property' decorator you can call the `_username` as if it were the actual attribute. 

```python

>>> temp_device_1 = NetworkDevice(host='host1.domain.com', platform='cisco_xe', username='admin', password='password123')
>>> temp_device_2 = NetworkDevice(host='host1.domain.com', platform='juniper_junos', username='admin', password='password123')
>>> print(temp_device_1.username, temp_device_1.password )
admin password123
>>> print(temp_device_1._username, temp_device_1._password )
admin password123

```
#### Example code 2
Here is actually a cool use by using getters and setters.
 ```python

class NetworkDevice:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self.username = username
        self._password = password


    @property
    def password(self):
        password_len = len(self._password) + 1
        return '*' * password_len
        
    @password.setter
    def password(self, new_password):
        print(f'You have reset your password')
        self._password = new_password

 
print(temp_device_1.username, temp_device_1.password )
temp_device_1.username, temp_device_1.password = "new_username", "New_Password"
print(temp_device_1.username, temp_device_1.password )
print(f'real password is: {temp_device_1._password} ')
```

#### Example return 2
```python 

# Here is the result
admin ************
You have reset your password
new_username *************
real password is: New_Password 

 ```


#### Example Code 3
```python 
class Interface:
    def __init__(
        self,
        intf_name,
        intf_mode="access",
        access_vlan=None,
        speed="1Gbps",
        duplex="full",
    ):
        self.intf_name = intf_name

        # These two attributes will use the @property.setter constraints defined below
        self.intf_mode = intf_mode
        self.access_vlan = access_vlan

        self.speed = speed
        self.duplex = duplex

    def __str__(self):
        if self.intf_mode == "trunk":
            return (
                f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, "
                f"Mode: {self.intf_mode})"
            )
        else:
            return (
                f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, Mode: {self.intf_mode}, "
                f"Vlan: {self.access_vlan})"
            )

    @property
    def intf_mode(self):
        return self._intf_mode

    @intf_mode.setter
    def intf_mode(self, value):
        if value in ("access", "trunk"):
            self._intf_mode = value
            if value == "trunk":
                self.access_vlan = None
        else:
            raise ValueError(f"Invalid value for intf_mode: {value}")

    @property #This is creating a method that is the same as the attribute 
    def access_vlan(self):
        return self._access_vlan

    @access_vlan.setter
    def access_vlan(self, value):
        if self.intf_mode == "access":
            if not isinstance(value, int):
                raise ValueError("Access VLAN must be an integer")
            self._access_vlan = value
        elif self.intf_mode == "trunk":
            self._access_vlan = None
```