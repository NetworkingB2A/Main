
class NetworkDevice:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        print(f'Set new username to: {new_username}')
        self._username = new_username

    @property
    def password(self):
        return '*' * len(self._password)
        
    @password.setter
    def password(self, new_password):
        if new_password == self._password:
            raise ValueError("You set your password the same as your current password")
        print(f'You have reset your password')
        self._password = new_password

    def __str__(self) -> str:
        return f' NetworkDevice: {self.host} ({self.platform})'

    @staticmethod
    def printer_hello(arg1='hello world'):
        print(arg1)

    


class Interface:
    def __init__(self, intf_name, intf_mode="access", access_vlan=1, speed="1Gbps", duplex="full"):
        self.intf_name = intf_name
        self.intf_mode = intf_mode
        self.access_vlan = access_vlan
        self.speed = speed
        self.duplex = duplex
        
        # Run checks
        self.intf_mode_check()
        self.intf_access_vlan_check()
    
    def intf_mode_check(self):
        if self.intf_mode in ['access', 'trunk']:
            pass
        else:
            raise ValueError('You did not pass in a access or a trunk mode')
    
    def intf_access_vlan_check(self):
        if self.intf_mode == 'access':
            if isinstance(self.access_vlan, int):
                pass
            else:
                raise ValueError('Access vlan is not int type.')
        else:
            self.access_vlan = None
        
    def __str__(self):
        if self.intf_mode =='trunk':
            return f'Interface: {self.intf_name} ({self.speed}/{self.duplex}, Mode: {self.intf_mode})'
        else:
            return f'Interface: {self.intf_name} ({self.speed}/{self.duplex}, Mode: {self.intf_mode}, Vlan: {self.access_vlan})'

temp_device_1 = NetworkDevice(host='host1.domain.com', platform='cisco_xe', username='admin', password='password123')
temp_device_2 = NetworkDevice(host='host1.domain.com', platform='juniper_junos', username='admin', password='password123')



print(temp_device_1.username, temp_device_1.password )
temp_device_1.username, temp_device_1.password = "new_username", "New_Password"
print(temp_device_1.username, temp_device_1.password )
print(f'real password is:  {temp_device_1._password} ')
temp_device_1.password = "New_Password"




"""
print(Interface(intf_name= 'Et1', speed= '1Gbps', duplex= 'full', intf_mode='access', access_vlan= 1))
print(Interface(intf_name= 'Et2', speed= '1Gbps', duplex= 'full', intf_mode='access', access_vlan= 2))
print(Interface(intf_name= 'Et3', speed= '1Gbps', duplex= 'full', intf_mode='access', access_vlan= 3))
print(Interface(intf_name= 'Et4', speed= '1Gbps', duplex= 'full', intf_mode='access', access_vlan= 4))
print(Interface(intf_name= 'Et5', speed= '1Gbps', duplex= 'full', intf_mode='access', access_vlan= 5))
print(Interface(intf_name= 'Et6', speed= '1Gbps', duplex= 'full', intf_mode='access', access_vlan= 6))
print(Interface(intf_name= 'Et7', speed= '1Gbps', duplex= 'full', intf_mode='trunk'))


apple = NetworkDevice.printer_hello()
NetworkDevice.printer_hello('spam and eggs. no bacon.')

"""
