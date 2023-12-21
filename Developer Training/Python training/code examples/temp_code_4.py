from dataclasses import dataclass

"""
class NetworkDevice:
    def __init__(self, device_type, hostname, host_ip_address, host_username, host_password ):
        self.device_type = device_type
        self.hostname = hostname
        self.host_ip_address = host_ip_address
        self.host_username = host_username
        self.host_password = host_password
    
    def __repr__(self):
        return f''' 
 NetworkDevice: 
     Device Type: {self.device_type
     Hostname: {self.hostname}
     Host IP Address: {self.host_ip_address}
     Host username: {self.host_username}
     Host Password: {self.host_password}
'''
        
    def __eq__(self):
        pass

new_network_device = NetworkDevice(
    device_type= "Firewall", 
    hostname="firewall01", 
    host_ip_address= "10.1.1.1", 
    host_username="pa_admin", 
    host_password= "pa_password")

print(new_network_device)
"""


@dataclass
class NetworkDevice:
    device_type: str
    hostname: str
    host_ip_address: str
    host_username: str
    host_password: str
    
new_network_device = NetworkDevice(
    device_type= "Firewall", 
    hostname="firewall01", 
    host_ip_address= "10.1.1.1", 
    host_username="pa_admin", 
    host_password= "pa_password")

print(new_network_device)