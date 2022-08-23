# Hello world Kubernetes

This is a hello world deployment using Kubernetes, Nginx Ingress Controller, simple Python app.

## Requirement installation

First of all, you need to install software below:

- Docker: [link](https://docs.docker.com/engine/install/)
- Minikube: [link](https://minikube.sigs.k8s.io/docs/start/)
- Kubectl: [link](https://kubernetes.io/docs/tasks/tools/)

## How to run

- Unzip file taz
- Check minikube install successfully: `minikube version`
- Check kubectl install successfully: `kubectl version`
- Check docker install successfully: `docker --version`
- Run command to start minikube: `minikube start`
- Check minikube run successfully: `kubectl get nodes`
- Enable the NGINX Ingress controller: `minikube addons enable ingress`
- Verify that the NGINX Ingress controller is running: `kubectl get pods -n ingress-nginx`
- Create a deployment using the following command: `kubectl create deployment python-app --image=ncongduy/python-app:v1`
- Check a deployment successfully: `kubectl get deployments`
- Expose the deployment: `kubectl expose deployment python-app --type=NodePort --port=5000`
- Verify the Service is created and is available on a node port: `kubectl get service python-app`
- Create the Ingress object by running the following command: `kubectl apply -f ./python-app-ingress.yml`
- Verify the IP address is set: `kubectl get ingress`
- Save `ADDRESS python-app.info` (for example `192.168.49.2 python-app.info`) to the bottom of the `/etc/hosts` file on your computer (you need administator access)
- Verify that the Ingress controller is directing traffic: `curl python-app.info`

## API of python app

- GET: python-app.info ==> "Home page"
- GET: python-app.info/forum ==> "Show articles"
- POST: python-app.info/forum ==> "Accepted"
- PUT: python-app.info/forum ==> "Updated"
- DELETE: python-app.info/forum ==> "Deleted"

We can check API via a command line in bash:

- `curl python-app.info`: receive a result "Home page"
- `curl python-app.info/forum`: receive a result "Show articles"
- `curl -X POST python-app.info/forum`: receive a result "Accepted"
- `curl -X PUT python-app.info/forum`: receive a result "Updated"
- `curl -X DELETE python-app.info/forum`: receive a result "Deleted"

## API of python app via NodePort

- Save url into environment variable: `export URL=$(minikube service python-app --url)`
- GET: `$URL` ==> "Home page"
- GET: `$URL/forum` ==> "Show articles"
- POST: `$URL/forum` ==> "Accepted"
- PUT: `$URL/forum` ==> "Updated"
- DELETE: `$URL/forum` ==> "Deleted"

We can check API via a command line in bash:

- `curl $URL`: receive a result "Home page"
- `curl $URL/forum`: receive a result "Show articles"
- `curl -X POST $URL/forum`: receive a result "Accepted"
- `curl -X PUT $URL/forum`: receive a result "Updated"
- `curl -X DELETE $URL/forum`: receive a result "Deleted"

## Reference

- Learn Kubernetes Basics: [link](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- Hello Minikube: [link](https://kubernetes.io/docs/tutorials/hello-minikube/)
- Install Tools: [link](https://kubernetes.io/docs/tasks/tools/)
- Set up Ingress on Minikube with the NGINX Ingress Controller: [link](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)
- Deploying a Flask Application on Kubernetes: [link](https://www.youtube.com/watch?v=-g9r8BSlDFI)
