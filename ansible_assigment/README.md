#

## Description

Current application take json via http POST and out what are animal say

Really, you can do somethink like this:

[![Demo](https://j.gifs.com/VvPJ2B.gif)](https://www.youtube.com/watch?v=jofNR_WkoCE)

Application listen tcp port 8080 on system. Nginx uset to proxy your request to application port.

With playbook.yml you can deploy this application on your server. Just follow intstructions

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

## Installation on target system

Run ansible playbook:

```sh
ansible-playbook --ask-become-pass -i ./inventory.yml ./playbook.yml
```

If you use password-base authentification run like this:

```sh
ansible-playbook --ask-pass --ask-become-pass -i ./inventory.yml ./playbook.yml
```

After this you need enter your root password. With ```--ask-pass``` enter your user password first.

## Usage

Use curl to POST json on target system:

```sh
curl -XPOST -d'{"animal":"{animalname}", "sound":"{sound}, "count": 3}' http://{target_ip_or_hostname}
```

## Examples

- Target system is Debian10 from netinstall
- Target ip - ```192.168.85.19```
- First connect to target after installation
- Destination hostname - ```vm1```

Installing :
[![asciicast](https://asciinema.org/a/c4BZOp87yCilSutAc4OfOICDL.svg)](https://asciinema.org/a/c4BZOp87yCilSutAc4OfOICDL)

Usage: 
```Coming soon```

```