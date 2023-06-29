Everything starts with a virtual network
- communications with the internet
- communication between azure resources




## Capabilities of Azure Virtual Networks
- Communication with the internet
- Communication between Azure resources
  - There are three key mechanisms through which azure resource can communicate: VNets, VNet service endpoint and VNet peering
- Communication between on-premises resources
  - Some options to connect to on-prem include: point-to-site VPN, Site-to-site VPN, Azure ExpressRoute
- Filtering network traffic
- Routing network traffic
  - You can implement route tables or BGP routes to override the default routes Azure creates.

## Design considerations for Azure Vitrual Networks
You can only use the RFC 1918 networks in azure.
Careful that you do not overlap subnets that are on-prem or other resource groups inside of azure subscription.
Azure will reserve 5 ip address from a subnet( example for a /24 network below)
- x.x.x.0: network address
- x.x.x.1: Reserved be Azure for the default gateway
- x.x.x.2,x.x.x.3: Reserved by Azure to map the Azure DNS IPs to the VNet space
- x.x.x.255: Network broadcast address

When designing in Azure there are some of the same principles as designing an on-prem network, but there are also going to be unique features as well. Some design considerations include:
- VNets
- Subnets
- Micro-segmentation
- Determine a naming convention
- Which regions or availability zones to put your resources in
  - There are three categories for availability zones:
    - Zonal services - Resources that are pinned to a specific Azure region
    - Zone-redundant services - Resources are replicated or distributed across zones automactically.
    - Non-regional services - Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.

### NOTES:
BastionHost: The Azure Bastion service is a new fully platform-managed PaaS service that you provision inside your virtual network. It provides secure and seamless RDP/SSH connectivity to your VM directly in the Azure portal over SSL. When you connect via Azure Bastion, your VM does not need a public ip address.