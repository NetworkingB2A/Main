## What is Cumulus Linux?
It is an Network operating system that is written on debian linux.

This part is actually Nvidia/Mellanox.
What is infiniband?
computer networking communication standard. used in high.performance computing. it has very hight throughput and very low latency. its used to connect compute resources, storage, server communications. Infiniband uses a technology that can utilize all layers of the OSI to move data as fast as possible.
Equipment needed for infiniband
- Switches
- Subnet manager manages all network activity
- Network adapters for the hosts
- gateway
  - This is used to allow infiniband devices and ethernet devices to talk to each other 
- infiniband router
  - used to allow infiniband networks to talk to one another  
Key features of infiniband
- simplified management
 - managed but the subnet manager
 - every subnet has its own subnet manager master
 - the second subnet manager is a standby
 - this is used for control plane traffic
- high bandwidth
 - started at 10 gb
 - currently is 400 gbps
- cpu offloads
  - hardware based transfer protocol
  - the application sends it data to the hardware level and is able to skip the kernel. this means the less cycles are hitting the cpu
  - RDMA(Remote direct memory access) NEED TO LOOK AT MORE
  - The gpus also have this same technology
- ultra low latency
- network scale out
  - You can deploy up to 48000 nodes on a single subnet
    - What is a node?
    - How big is a subnet?
    - ip addressing?
- OQS
- fabric resiliency
  - Self healing recovery
    - if a link failure happens the recovery time take 1 Millisecond
- optimal load-balancing
  - adaptive routing is an option for load balancing. ( its like ecmp) 
  - enabled on the hardware
  - controlled by adaptive routing manager
  - the queue manager watches all of its links
  - the queue manager will send out data based on the data it has gathered
- sharp (scalable hierarchical aggregation and reduction protocol) MPI super performance
  - Sharp helps reduce the data traversing the network
- Variety of supported topologies
  - fat tree
  - torus
  - dragonfly+
  - hypercube
  - hyperX
infiniband architecture 
- Applications can talk to each other without going though the OS
- layers
  - upper layer
    - describes the how Applications use the Infiniband system 
      - some protocols used by the uppper layer include
        - MPI - Message passing interface
        - NCCL - NVIDIA collections communication library
        - iSER - RDMA storage protocols
        - IPoIB - ip over infiniband
  - Transport layer
    - A tunnel is created between two apps
  - network layer
  - Link layer
    - local ID or LID 
    - flow control
  physical layer 