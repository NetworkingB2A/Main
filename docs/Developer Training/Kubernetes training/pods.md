Kubernetes does not deploy containers directly on the worker nodes. The containers are encapsulated into a pod. A pod is a single instance of application. a pod is the smallest objects you can create in kubernetes.

### how to deploy a pod
kubectl run {name of image for pod} --image {name of the image you are trying to install}
kubectl run nginx --image=nginx #This will go to docker hub by default and pull ht nginx image down.

kubectl get pods # this will show the pods with the default namespace.
kubectl describe pod {name of pod} # this will tell you a lot of info about the pod.
kubectl describe pod -o wide # another way to find out more info about a pod.

Under the ready 1/2, the first number is the number of running pods, the next number is the total number of pods.
controlplane ~ ➜  kubectl get pods 
NAME            READY   STATUS             RESTARTS   AGE
nginx           1/1     Running            0          8m6s
newpods-bgmdp   1/1     Running            0          5m58s
newpods-lgwkb   1/1     Running            0          5m58s
newpods-tlrw9   1/1     Running            0          5m58s
webapp          1/2     ImagePullBackOff   0          3m54s

### Yaml for Kubernetes

There are always 4 top level fields in the deployment yaml file.

- apiVersion - This is the api version of kubernetes you are using. Based on the type of container you are using the version could be different. example
| Kind | Version |
|-|-|
| POD | v1 |
| Service | v1 |
| ReplicaSet | apps/v1 |
| Deployment | apps/v1 |
- kind - This is the type of object you are trying to create.
- metadata - Data about your pod
- spec - additional info to kubernetes about the pod you are creating

Example of a yaml file
```yaml
apiVersion: v1                          
kind: Pod
metadata:
  name: myapp-pod
  labels: 
    app: myapp
    type: front-end
spec:
  containers:
    - name: nginx-container
      image: nginx
```

