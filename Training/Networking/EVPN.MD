Why EVPN?
One reason is moving VMs into different segments of the data center without changing their IP address. Vmotion
Industry standard


What is needed to build an EVPN Network?
- Topology (leaf/Spine)
- Underlay
  - OSPF - IP unnumbered
  - ISIS - IP unnumbered
  - iBGP - IP numbered
  - eBGP - IP numbered
- Overlay
  - MP-BGP
    - evpn address family is the standard
    - What will we be learning in MP-BGP
      - Mac address
        - You are effectively routing MAC address around
      - IP host/32
      - IP network
    - LOTS OF BGP PEERING. Peer groups will be your friend here.
    - if you choose eBGP. one idea is to have your spines be the same AS. and maybe even segment your leaves into groups of the same AS.
- You should use automation when deploying EVPN.
- NOTES
  - Although this is not required its kind of a industry standard
    - Loopback 0 - Overlay Routing protocol
      - Every device will get a loopback 0 for routing 
    - Loopback 1 - VTEP Address
      - Generally Loopback 1 is only on the leaves where the VTEP exists.

VRF
- Logically separate routing table.
- gives you a way to separate data on a device. You can also use the same ip address on device. 
- If you want the VRFs to talk. they must meet and exchange routes
- normally i see that each vrf has its own separate link. but what happens when you have only 1 link between 2 devices?
  - Route Distinguishers and Route Targets
    - Route Distinguishers
      - This will allow you to tell if the difference between two routes that are the same in the same route table
      - This makes each route unique in the routing table. that is all it does.
      - This may never match between routes and sites. and this works well because it one extra level to help you troubleshoot an issue. a lot of time the loopback of the device is used as the route distinguisher
    - Route Targets
      - is it metadata, 
      - You would use an import and export statement.
      - you export your route with a tag. then on the the other device you would import that tag and drop that route into the vrf that you want to.
      - This must match on every device for the VRF you care about
Three different VRF you will use on every device
- Default
  - this is down with the normal command <code>ip vrf</code>
- Mac VRF (L2VNI)
  - used for Mac address
  - This is done as a vlan on the switch
  - in EVPN if you are using physical switches every VNI must have a Vlan tied to it. every vlan has a VNI tied to it. 1 to 1 mapping
  - the data is like a normal mac table. it is also called a stretched vlan.
  - It is just like a bridging table.
  - Type 2 route - going to have a RD and a RT 
  - All of this is done at the control plane. meaning that each packet knows where to go, and no cpu needs wasted at the data plane layer. 
  - normally you would have to send a frame with a vlan tag. and that tag is stripped off at the data layer. costing cpu and slowing down the process because of the extra step.
  - This will not take up any CAM to TCAM space
  - Spanning tree will still be running but its only to protect you if you decide to plug a switch into a switch. Not for actual data.