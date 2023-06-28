## SDN and IBN
Software defined networking and Intent based networking
SDN is a building block of IBN

### SDN
SDN characteristics and components are as follows:
- Network devices - These devices talk to the SDN controller on the controllers southbound interfaces
- SDN controller - Brains of SDN, communicates with network devices, applications and services using APIs
- Southbound interface - The interface the SDN talks to the down stream devices.
  - Southbound controller protocols
    - OpenFlow
    - NETCONF
    - RESTCONF
    - OpFlex
    - REST
    - SNMP
    - Vendor-specific protocols
- Northbound interface - The interface that talks with applications and services
- Network management applications and services

SDN Benefits
- Centralized Provisioning
- Network security
- Faster Deployments
- Programmable

### IBN
Intent enables the express of both business purpose and network context through abstractions, which are translated to achieve the desired outcome for network management.

The three foundational elements of IBN are as follows:
- Translation - What to accomplish, not how.
- Activation - This part deploys the policies from the translation element.
- Assurance - This part verifies the continue operations and the activation happened properly.

IBN Characteristics
- Translation and validation
- Automation
- State awareness
- Assurance and optimization

IBN Benefits
- Reduced complexity
- Simplifies deployment
- Strengthens security
- Improves agility
- Eliminates repetition