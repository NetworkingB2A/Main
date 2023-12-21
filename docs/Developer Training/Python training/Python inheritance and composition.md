# Inheritance vs Composition
Inheritance should be used with a 'is a' relationship.
- NetworkDevice as the super class, and a Router 'is a' NetworkDevice.
Composition should be used with a 'has a' relationship.
- A Router class 'has a' NetworkInterface class.

## Inheritance 
### What is inheritance? 
Inheritance is the idea of a class that can use a higher level classes methods and attributes.
Example
I have a `NetworkDevice` class that has a `ip_address` attribute. I create a `Router` class and I dont want to create another `ip_address` attribute. I can just inherit the `NetworkDevice` class and when someone create a `Router` object, they will need to put in a `ip_address` attribute. 

### Gotchas
Here is one potential problem you need to be aware of and look out for. In example code 1 below, I created a `NetworkDevice` class, and a `Router` class. The `Router` class inherits from the `NetworkDevice` class. I did not code the `__repr__` very well and when I went to print the temp_router, You see the repr is saying the router is a `NetworkDevice` object.

A better way to code the `NetworkDevice` class is shown in example NEED TODO:

Example Code 1
```python
class NetworkDevice:
    def __init__(self, hostname, host_ip_address, host_username, host_password ):
        self.hostname = hostname
        self.host_ip_address = host_ip_address
        self.host_username = host_username
        self.host_password = host_password

    def __repr__(self):
        return f''' 
 NetworkDevice: 
     Hostname: {self.hostname}
     Host IP Address: {self.host_ip_address}
     Host Username: {self.host_username}
     Host Password: {self.host_password}
'''
        
class Router(NetworkDevice):
    pass

temp_router = Router(
    hostname="router1", 
    host_ip_address= "10.1.1.1", 
    host_username="router_admin", 
    host_password= "router_password")

print(temp_router)
```
Example output 1

```python
 
 NetworkDevice: 
     Hostname: router1
     Host IP Address: 10.1.1.1
     Host Username: router_admin
     Host Password: router_password
```

Example Code 2
```python
class NetworkDevice:
    def __init__(self, hostname, host_ip_address, host_username, host_password ):
        self.hostname = hostname
        self.host_ip_address = host_ip_address
        self.host_username = host_username
        self.host_password = host_password

    def __repr__(self):
        return f''' 
 NetworkDevice: 
     Hostname: {self.hostname}
     Host IP Address: {self.host_ip_address}
     Host Username: {self.host_username}
     Host Password: {self.host_password}
'''
        
class Router(NetworkDevice):
    def __repr__(self):
        return f''' 
 Router: 
     Hostname: {self.hostname}
     Host IP Address: {self.host_ip_address}
     Host Username: {self.host_username}
     Host Password: {self.host_password}
    pass

temp_router = Router(
    hostname="router1", 
    host_ip_address= "10.1.1.1", 
    host_username="router_admin", 
    host_password= "router_password")

print(temp_router)
```
Example output 2

```python
 
 Router: 
     Hostname: router1
     Host IP Address: 10.1.1.1
     Host Username: router_admin
     Host Password: router_password
```


## Composition
