#

## Desription

This is a docker file to build image with [zoo_app](../ansible_assigment/zoo_app).
After run container listen port 8080. See more information about zoo_app in my [repository](../ansible_assigment/README.md)

## Requirements

- [Install docker](https://docs.docker.com/get-docker/) on your system
- Internet connection

## Installation

Copy dockerfile to your system, cd to same directory and run:

```sh
docker build . -t {image_name}
```

After succesful build run container:

```sh
docker run -d -p 8080:8080 {image_name}
```
