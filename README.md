# Kubernetes hello world

This repository contains:
* simple test python web application. With two API methods /hello and /health
* helm configuration for deployment in local k8s cluster

Helm configuration contains:
* Deployment configuration
* Service configuration with cluster ip
* Ingress configuration

## Pre-Request 

* Docker
* Docker-compose (optional)
* Helm
* Python 3
* Local k8s cluster (docker-desktop / minikube)

## Installations

### Docker and kubernetes cluster

Before deployment you must install local kubernetes cluster. For Mac and Windows you can use Docker Desktop. For linux minikube. 

#### Mac:
    First install Docker Desktop 
        https://hub.docker.com/editions/community/docker-ce-desktop-mac
    Second enable kubernetes in Docker Desctop
        docker desctop->preferences->kubernetes
        https://rominirani.com/tutorial-getting-started-with-kubernetes-with-docker-on-mac-7f58467203fd
    
#### Minikube (linux)
    https://kubernetes.io/docs/tasks/tools/install-minikube/
    
    After installing minikube run this commands in terminal:
    
    ```
        minikube start
        
        # Build stage doesn't push image to external hub. This command needed to build image inside minikube
        eval $(minikube docker-env)
    ```
    
### Ingress
    
    Foolow this documentation to install ingress for your platform
    https://kubernetes.github.io/ingress-nginx/deploy/
    
### Helm

    Foolow installation guid
    https://helm.sh/docs/install/#installing-helm
    
    After installation initialize helm
    
    ```
        helm init
    ```
    
### Install Web api dependency

This command installs python package dependency
```
    make install 
```

## Test

Run local unit tests
```
    make test
```

As alternative there is docker compose file that can run tests without python installation.

```
    docker-compose build test
    docker-compose run test
```

    
## Deployment

Deployment to local k8s cluster. Deployment creates all components in **hello-world** namespace.

```
    make build
    make deploy
```

Test deployment:
```
    make smoke-test
```

Alternatively without python installation
```
    # For docker desctop
    curl http://localhost/hello-world/health
    # For minikube
    curl http://$(minikube ip)/hello-world/health
```

Cleanup kubernetes from api deployment
```
    make cleanup
```

## Notes and Issues

Project was tested on two environment: 
* Mac - Docker Desktop 2.0.0.3; Engine: 18.09.2; Kubernetes: v1.10.11; helm 2.14.1
* Ubuntu - minikube v0.33.1; helm 2.14.1

Issues: 
    make file not fully automized - required manual command (eval $(minikube docker-env))
    
    
## TODO

* automized installing ingress based on OS
* Push image to external repository
* Logging
* Metrics and monitoring