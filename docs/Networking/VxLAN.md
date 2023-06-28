What is VxLan?  
- it it helps reducing the need for Spanning tree, trucking  
- It allows you to put a Layer 2 network overlay with a layer 3 underlay  
- Standard based - RFC XXX  

Vlan 
- id is 12 bits long
- which allows for 4095 vlans
- Concept if you have customers in your data center
  - if you gave each customer 8 vlans, you only have room for 511 customers

VxLan
- VNI = VxLAN Network Identifier
- A VNI is a bridge domain
- Traffic is encapsulated with UDP and IP 
- VNI work just like Vlans. if you want to go between VNIs you will need a router.
- Changes to the Underlay does not impact the Overlay. as long as there is ip connectivity.
- id is 24 bits long
- 16,777,216 segments
- VNI can be created as a 
  - L2VNI
    - used for bridging
    - Used when traffic is located in the same lan segment.
  - L3VNI
    - Used for Routing
    - When traffic need to leave a L2VNI
    - Optional ( but needed if you want to route on the local switch)
    - All VTEPs need to learn about all L3VNIs
      - This is to support a feature called Anycast Gateway
      - Each switch acts as a default gateway for the hosts in that VNI
      - Every switch will have the same IP address and the same virtual MAC address.
      - No need for timers like HSRP or other FHRP.
      - All hosts can have a same default gateway. doesnt matter what switch they are connected to.
    - Mulitentacny 
      - L3VNI are attached to a VRF
      - Many VNIs can be associated with a Customer or Tenant 
      - Routes and route tables will be kept separate by using Route distinguisher and route targets.

VTEPs
- Basics
  - Is a special kind of interface  
  - VTEPs connects the overlay to the underlay
  - VTEP has a ip address in the underlay and 1 or more VNIs
  - traffic between a source and destination VTEP create a stateless tunnel. the tunnel is formed long enough to pass the VxLan frame in the tunnel
  - When traffic comes to a VTEP, the VTEP will encapsulate the traffic and sent that traffic to the remote VTEP to be decapsulated.
  - The VTEPS are on the leaf switches.
  - VxLAN tunnels are created on leaf switches.
  - If you use BGP Spine switches can become Route-Reflectors.
- Address learning
  - Data Plane Learning (This is the older Method)
    - flooding learning
    - ARP 
    - No build in support for routing
    - if you want to go between VNIs you need to have an external router
  - Control Plane Learning (Newer way of address learning)
    - More efficent
    - The switches learn about the mac address before they are needed.
    - Switches peer with each other.
    - This uses the EVPN address family
  - Traffic types
    - Unicast traffic
    - BUM Traffic (Traffic that goes to more then one destination)
      - BUM traffic Type
        - Broadcast
        - Unknown Unicast
        - Multicast
      - How to handle BUM traffic
        - Multicast
          - Each VNI is matched to a single Multicast group
          - Each Multicast group may match to 1 or more VNI
          - When a VTEP comes online, the VTEP will use IGMP to join the multicast group that it uses.
          - When VTEP needs to sent BUM Traffic, the VTEP will only to the relevant multicast group.
          - Could be complicated, based on your multicast environment. 
        - Headend replication 
          - Must use BGP with EVPN 
          - When BUM traffic arrive, the VTEP will send multiple unicast traffic packets to the other VTEP that support that VNI
          - Does not scale as well, but is much simpler to implement. 
          - One recommendation is 20 VTEPs or less ( 20 leaf nodes)

How does a Host talk to another host?
- all Switches must run iBGP
- A full mesh must be created or route reflectors must be used.
- When a switch is added that is running a VTEP. That switch will learn where all of your other VTEPs are.
- When VTEPs are added through BGP. Those VTEPs are added to a white list. All other VTEPs are untrusted.
- BGP authentication would be good idea to eliminate rogue peers. 
- host MAC Address are added to the local BGP process. The host is discovered when they start up. The host MAC address is shared with all BGP peers. When a host sends another host data, the switch looks up the other host with BGP.
- You will be using ARP surpression. but the host will still need to use ARP. but the ARP request will go the Switch. the switch will know the MAC address of the remote host and end up sending the ARP right back without flooding the other switches.

Encapsulation of a data using VxLAN
Ethernet|IP|UDP|VxLAN|frame

VxLAN header -  Total of 64 Bits
reserved - 8-bits
VNI - 24-bits: The VxLAN ID
Reserved - 24-Bits
Flags - 8-bit; Bit-3 shows VNI is valid

Things to know
- UDP destination port is 4789 
- Know that you will need to have Jumbo frames enabled for best results
- ECMP (Equal-cost Multipath) routing will help significantly with this strategy. 
- if your fabric starts to grow too large, you can break up the design into more spine/leaves. At this point you would add a Super-spine. (Not used very often)

What about Routers/Firewalls/Load Balancers/ETC?
- This functionality is added to the Leaf layer.
- When routers/Firewalls are added to a leaf, the leaf becomes a boarder leaf.
- Boarder leaf switches represent connectivity to and from the fabric.


Thoughts to help me understand
- it seems like frame that is already constructed goes to the VTEP. The VTEP encapsulated the frame adds VxLAN tag( for lack of a better word). once the frame has the new VxLAN header, the frame brought back up to layer 4, and starts again.


















!!!! Not sure where to put this yet. but Need to take the notes


