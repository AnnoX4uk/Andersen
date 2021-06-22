#

- [Description](#description)
  - [Features](#features)
  - [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Description

This is a golang writen bot for Telegram messenger. Simpe for install, simple to use. This bot can rescieve some information about your user and his repository on github. Then you can create bot and send some commands for him to rescieve information about complated tasks.

### Features

- [x] Golang compile application
- [x] Worked with Telegram
- [x] Support Telegram commands
- [x] Answer about user git repository with http link
- [x] Answer about tasks
- [x] Answer about task by number with link to task
- [x] Already worked in Telegram
- [ ] 🔜 Answer about **complited** tasks
  
### Requirements

- golang
- github.com/Syfaro/telegram-bot-api

## Installation

Before start you need to create bot in Telegram with @BotFather ([see documentation 📖](https://core.telegram.org/bots)) and add some commands to new bot:

```code
/git
/tasks
/task
```

Clone this repository.
Check all requiret modules are installed. If not, install them:

``` bash
go get github.com/Syfaro/telegram-bot-api
```

Compile app with next command:

```bash
go build tgbot.go
```

Edit config.json with your github user, github repo and Telegram bot Token.

```json
{
    "Name": "username",
    "Reponame": "repository_name",
    "Token":"telegram_token"
}
```

Run tgbot and enjoy!

## Usage

To use bot you must add him to your chat and send commands for him.
```/git``` will return link to git repository
```/tasks``` will return list of tasks
```/task #``` will return link to task number #

Invite **@AndersenCourseTG_bot** and test them all
