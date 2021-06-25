#

- [Description](#description)
- [What we do](#what-we-do)
- [Requirements](#requirements)
- [Prepare installation](#prepare-installation)
- [Installation on target system](#installation-on-target-system)
- [Usage](#usage)
- [Examples](#examples)

## Description

Current application take json via http POST and out what are animal say

Really, you can do somethink like this:

[![Demo](https://j.gifs.com/VvPJ2B.gif)](https://www.youtube.com/watch?v=jofNR_WkoCE)

Application listen tcp port 8080 on system. Nginx uset to proxy your request to application port.

With playbook.yml you can deploy this application on your server. Just follow intstructions

## What we do

- [x] Copy your ```id_rsa.pub``` to target system
- [x] Disable RootLogin
- [x] Disable PasswordBase authentification
- [x] Enable public-key authentification
- [x] Install pim, iptables and nginx
- [x] Install ```zoo_app``` required modules
- [x] Set zoo_app default host for nginx
- [x] Create (if not_exist) ```/opt``` directory
- [x] Create zoo_app service and set autostart it.
- [x] Allow incoming connections only for 22,80,443 tcp ports

## Requirements

- Debian 10 with worked sshd service as destination target
- Python3 installed on **target** system
- Installed ansible on **your** system
- If you use password-base authentification on your target system (with first connect) also you need install sshpass.

## Prepare installation

Copy [this](ansible_assigment/) directory to **your** system.
Configure ```inventory.yml``` with your destination system

```yml

{groupname}: 
   hosts:
        {hostname}:
          ansible_ssh_host: {destination_ip}
          ansible_python_interpreter: /usr/bin/python3
  
```

Prepare ```id_rsa.pub``` in your ```{UserHomeDirectory}/.ssh/``` directory. If your key stored at another place - modify ```Copy public key``` task with right path.

## Installation on target system

Run ansible playbook:

```sh
ansible-playbook --ask-become-pass -i ./inventory.yml ./playbook.yml
```

If your target system use password-base authentification run like this:

```sh
ansible-playbook --ask-pass --ask-become-pass -i ./inventory.yml ./playbook.yml
```

## Usage

Use curl to POST json on target system:

```sh
curl -XPOST -d'{"animal":"{animalname}", "sound":"{sound}", "count": 3}' http://{target_ip_or_hostname}
```

## Examples

- Target system is Debian10 from netinstall
- Target ip - ```192.168.85.19```
- First connect to target after installation
- Destination hostname - ```vm1```

![Demo](https://media.giphy.com/media/p4JmioGaHx964p7cai/source.gif)
