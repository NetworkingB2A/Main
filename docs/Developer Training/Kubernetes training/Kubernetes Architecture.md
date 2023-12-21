What is a node?
it is a machine. it is a worker machine. This is what will be launched by Kubernetes.

What is a cluster?
A cluster is a set of nodes grouped together.

What is a Master?
A Master is a node with kubernetes installed and is configured as the master. The master will watch over the other nodes and is responsible for the actual orchestration over the other nodes.

When you install kubernetes on a system, you are actually installing the following components.
- Api server - This is the front end for kubernetes. This is how a user interacts with Kubernetes.
- etcd - This is key-value keystore. it is created for managing the cluster and holds all the info about the cluster. Logs are also stored here to make sure there are not conflicts between any masters.
- Kubelet - This is the agent that runs on each node in the cluster. This makes sure the containers are running as expected.
- container runtime - This is the underlying service used to run containers. a lot of times this is docker, but there are other options as well.
- controller - this is the brains. it watches for nodes going down and it makes up decisions to bring up new containers. 
- scheduler - used for scheduling work across multiple nodes. looks for newly created containers and assigns them to nodes.
kubectl is used as a command line interface for kubernetes.
Look at the image below to see how all of these components work together.
TODO: insert image here


What is a replication controller and a replica set?
It allows you to run multiple instances of a container to allow for failure if the container fails in your pod. This will help with high availability. The replication controller will bring up a container when the container fails, and this is true even with single container pods.
A replication controller will also help with load balancing and scaling as well.

A replication controller is the older technology that is being replaced by replica set.

replica sets also have an extra field in the yaml file that is called the selector.


What are labels and selectors?
Labels are like tags. and you can filter based off labels.

What is a kubernetes deployment?
A deployment allows you to perform any of the following tasks
- deployment of pods or replicasets
- upgrade the replicasets or pods seamlessly.
- rolling updates. Updating one pod at a time.
- undo changes
- pause changes
- resume changes
You will need to create a deployment definition file.

Pods are in replicasets, replicasets are part of a deployment.


Kubernetes services help us connect other applications together or connects users to our apps. example if you have a front end pod, a back end pod and a database pod. the services help us connect them together. 

Types of services
Node port - A node port service will listen to port on the node and will port forward requests to the pod.
cluster ip - the service creates a virtual ip that allows different services to talk with each other
load balancer - it allows load balancing on the node.  