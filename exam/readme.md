#

## Description

This is exam lab for Andersen DevOps courses.

## Tasks

- [x] Develop 2 web applications with output ```Hello world 1``` and ```Hello world 2``` with language from list:
  - Python
  - Golang (gin framework)
  - PHP
  - .NET Core
  - Java
- [x] Build infrastructure with automated build and deploy application

### Hello world-go

The first language i chose Golang, because i have never worked in it before(except this course).

I will place application repository [here](https://github.com/AnnoX4uk/helloworld-go)
In ```helloworld-go``` folder i place configuration file for ```terraform```

### Hello world - python

The second language i chose Python, because it is wery simple for this task.

I will place application repository [here](https://github.com/AnnoX4uk/helloworld-python)
In ```helloworld-python``` folder i place configuration file for ```terraform```

### How it works

Clone this repo and run terraform with your api-key.

```sh
cd ./helloworld-go 
terraform plan
terraform apply
```

Then, ```terraform``` create new application in [Digital Ocean](http://digitalocean.com) cloud and deploy ```helloworld-go``` container. Use same way to deploy ```helloworld-python``` application.

After each commit to *main* branch of application repository, Digital Ocean rescieve new version from git and deploy it.

I think it is easiest way to deploy simple application in cloud.

### Need to do

- Monitoring all processes. Right now, i dont know then new version of application deploy, status of deploy, work application or not. This is a very very bad.
- Logging. It is simple, but very effective way for debugging.
- Infrastructure. Right now, it is two simple application. I think, if i have more time, i will place two instance to AWS or DO for each application in different zones, make nginx proxy and set up load-balancer.
- Tests. I have not enough time to write correct unit/integration tests, i never do it before. I think i will do it later.
