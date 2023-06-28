What is the Hierarchical design?
- Used in campus networks mainly.
- Relies on north/south traffic.
- Must use the core often  
- Lots of spanning tree/Trunks/Port-channels
- if you move from one area to another. your device will need a new ip address.
- Or you can send the Layer-2 vlans across the access layer. but this will increase the broadcast traffic as well as the layer 2 failure domain size. And this will only work at the distribution layers because the core is routed network.
- This design works at the campus because DHCP can hand out new ip address. but this will not work in the DC where most hosts have static ip address.  
![Picture of the common campus design](../images/Hierarchical.png)


What is Spine/leaf?
- There are only two levels.
- Every leaf switch connects to every spine.
- A host is at most 2 switch hops away to a destination
- Every connection between a leaf and spine must have a ip address.
- Spine switches are never connected to each other, and leaf switches are never connected to each other. 
  - This is true in most cases except for VPC. In this case two switches would have a Layer 2 peer link and a layer 3 keep alive. And these links are used for VPC traffic only
- This design will allow for east west traffic.  
![Picture of the common Data center design](../images/Spine-Leaf.png)

