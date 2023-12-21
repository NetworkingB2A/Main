from typing import Optional


# This class is being created so I can show composition
# A Router has a NetworkInterface
class NetworkInterface():
    def __init__(self, interface_name, speed = '1 gbps', duplex = 'auto', interface_ip_address = None):
        self.interface_name = interface_name
        self.speed = speed
        self.duplex = duplex
        self.interface_ip_address = interface_ip_address

    def __repr__(self):
        return f'''
Network Interface:
    Interface Name:        {self.interface_name}
    Interface Speed:       {self.speed}
    Interface Duplex:      {self.duplex}
    Interface Ip Address:  {self.interface_ip_address}
        '''



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

    def print_ip_address(self):
        return f'The host ip address is: {self.host_ip_address}'

# Here is an example of inheritance 
# Router is a Network Device.
class Router(NetworkDevice):
    def __init__(self, hostname, host_ip_address, host_username, host_password, network_interface, routing_protocol = "static"):
        self.routing_protocol = routing_protocol
        if isinstance(network_interface, NetworkInterface):
            self.network_interface = network_interface
        else:
            raise ValueError("you did not pass in a NetworkInterface object.")
        super().__init__(hostname, host_ip_address, host_username, host_password)


    def __repr__(self):
            return f''' 
Router: 
    Hostname: {self.hostname}
    Host IP Address: {self.host_ip_address}
    Host Username: {self.host_username}
    Host Password: {self.host_password}
    Routing Protocol: {self.routing_protocol}
    Network Interface:  {self.network_interface}
'''
    def print_ip_address(self):
        return super().print_ip_address() + f'\n The routing protocol for this IP Address is {self.routing_protocol} '


new_network_device = NetworkDevice(
    hostname="network_device", 
    host_ip_address= "10.0.0.1", 
    host_username="device_admin", 
    host_password= "device_password")

print(new_network_device)

print(new_network_device.print_ip_address())

new_interface = NetworkInterface(interface_name = 'eth1/1', interface_ip_address = "10.10.10.10")

print(new_interface)



new_router = Router(
    hostname="router1", 
    host_ip_address= "10.1.1.1", 
    host_username="router_admin", 
    host_password= "router_password",
    network_interface= new_interface)

print(new_router)

print(new_router.print_ip_address()+ "\n \n")
try: 
    fail_router = Router(
        hostname="router_fail", 
        host_ip_address= "100.100.100.100", 
        host_username="router_admin_fake", 
        host_password= "router_password_superfake",
        network_interface= "interface e1/1")
except ValueError:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nCould not create Router object\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
"""
Testing out a failing router
fail_router_temp = Router(
    hostname="router_fail_2", 
    host_ip_address= "100.100.100.100", 
    host_username="router_admin_fake", 
    host_password= "router_password_superfake",
    network_interface= "interface e1/1")
"""