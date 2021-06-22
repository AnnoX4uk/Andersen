#

- [Description](#description)
  - [Rules](#rules)
- [Homeworks](#homeworks)
- [Homework status](#homework-status)

## Description

In this repository storage homeworks of Andersen DevOps courses 📚.

Course started at May 31.

### Rules

- 1️⃣ repository
- 1️⃣ directory for one task
- ```README.md``` in all dirs

## Homeworks

<details>
<summary> Task 1 - Ansible assignment</summary>


```markdown
# Ansible assignment
## Create and deploy your own service
### The development stage:
For the true enterprise grade system we will need Python3, Flask and emoji support. Why on Earth would we create stuff that does not support emoji?!

* the service listens at least on port 80 (443 as an option)
* the service accepts GET and POST methods
* the service should receive `JSON` object and return strings in the following manner:
 \```sh
curl -XPOST -d'{"animal":"cow", "sound":"moooo", "count": 3}' http://myvm.localhost/
cow says moooo
cow says moooo
cow says moooo
Made with ❤️ by %your_name
curl -XPOST -d'{"animal":"elephant", "sound":"whoooaaa", "count": 5}' http://myvm.localhost/
elephant says whoooaaa
elephant says whoooaaa
elephant says whoooaaa
elephant says whoooaaa
elephant says whoooaaa
Made with ❤️ by %your_name
 \```
* bonus points for being creative when serving `/`

### Hints
* [installing flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation)
* [become a developer](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [or whatch some videos](https://www.youtube.com/watch?v=Tv6qXtc4Whs)
* [dealing with payloads](https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask)
* [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.get_json)
* [The database](https://emojipedia.org/nature/)
* 🐘 🐮 🦒
* what would you expect to see when visiting a random unknown website?

### The operating stage:
* create an ansible playbook that deploys the service to the VM
* make sure all the components you need are installed and all the directories for the app are present
* configure systemd so that the application starts after reboot
* secure the VM so that our product is not stolen: allow connections only to the ports 22,80,443. Disable root login. Disable all authentication methods except 'public keys'.
* bonus points for SSL/HTTPS support with self-signed certificates
* bonus points for using ansible vault

### Requirements
* Debian 10
* VirtualBox VM
```

</details>

<details>
<summary> Task 2 - Bash netstat</summary>

```sh
sudo netstat -tunapl | awk '/firefox/ {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n5 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F':' '/^Organization/ {print $2}' ; done
```

- Rework command to script
- Create ```README.md```
- Script can input PID or process name
- Count of lineout can be changed by user
- Feature to search other connections
- Simple and understandable errors output
- Have not depency of root rights, just warnings
- ⭐ Count connections to organization
- ⭐ Have another information from whois
- ⭐ Work with ss and use other utilites
</details>

<details>
<summary> Task 3 - Golang Telegram bot</summary>

- Worked Telegram bot
- Writen on Golang
- Use 3 commands:
  - ```/git``` - Get link on your github repository
  - ```/tasks``` - Get your task list
  - ```/task#``` - Get link on task {#}

</details>

<details>
<summary> Task 4 - Github creativity</summary>

```markdown
## Unleash your creativity with GitHub
* write a script that checks if there are open pull requests for a repository. An url like "https://github.com/$user/$repo" will be passed to the script
* print the list of the most productive contributors (authors of more than 1 open PR)
* print the number of PRs each contributor has created with the labels
* implement your own feature that you find the most attractive: anything from sorting to comment count or even fancy output format
* ask your chat mate to review your code and create a meaningful pull request
* do the same for her xD
* merge your fellow PR! We will see the repo history

### Hints
* [Have a look here](https://github.com/trending)
* read about GitHub API
* make use of curl and jq
```

</details>

<details>
<summary> Task 5 - Docker container </summary>

Build docker container for application from Task 1

- this time needs to listen port 8080, HTTP only
- light image size
- ⭐ use minimal possible setup

</details>

<details>

<summary> Task 6 - Cloud formation setup </summary>

- Write AWS CloudFormation template for diagram
  
![AWS diagram](https://imgur.com/n9zAcHn.png)

</details>

## Homework status

| Task                  | Status                  | link                              |
|-----------------------|-------------------------|-----------------------------------|
| Ansible assignment    | work in progress    70% | [zoo_app](ansible_assigment/)     |
| Bash netstat          | complete                | [netstat_script](netstat_script/) |
| Golang Telegram bot   | work in progress  95%   | [tg_bot](tg_bot/)                 |
| Github creativity     | not started             |                                   |
| Docker container      | not started             |                                   |
| Cloud formation setup | not started             |                                   |

