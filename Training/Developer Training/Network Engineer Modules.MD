
### Connection based Modules

scrapli (core) - 

request

ncclient: This python library helps with client-side scripting and application integration for the NETCONF protocol.

Netmiko: This module helps to make SSH connections, this for network devices. This really only supports the major vendors.


### Configuration Management

napalm: napalm (Network automation and programmability abstraction layer with multi-vendor support) is a python module that provides functionality that works in a multi-vendor fashion.

scrapli (extensions) - 

### Inventory Management

nornir: This is an extendable, multithreaded framework with inventory management to work with large number of network devices. This also works with your configuration platform. Just remember that nornir is a pythonic way of doing many tasks to many devices at one time, and a way of managing your inventory.


### Parsers and Data interpreters

Genie (PYATS)

xmltodict << These two are more generally used because of their ease of use.
untangle
minidom
ElementTree << These two are more generally used because of their ease of use.

pyyaml
ruamel.yaml << Currently this one is newer and better maintained.

pyang

json

csv


### Unit testing

pyats

unittest


### Operating system

sys: This module allows you to interact with python interpreter and manipulate and view values.

os: This module gives you access to the underlying operating system environment and file system. 


### Other

ipaddress module

pprint

pysnmp


datetime

time


## Additional Notes
- Scrapli
  - core
    -  pip install scrapli[genie]
  - nonir_scrapli
  - scrapli_community
    - This is for if you want to support addtional plateforms that are not supported by core.
  - scrapli_cfg
  - scrapli_replay
  - scrapli_netconf