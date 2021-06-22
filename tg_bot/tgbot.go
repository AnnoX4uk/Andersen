package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"

	tgbotapi "github.com/Syfaro/telegram-bot-api"
)

type Configuration struct {
	Name     string
	Reponame string
	Token    string
}

func getargs() Configuration {
	file, _ := os.Open("config.json")
	defer file.Close()
	decoder := json.NewDecoder(file)
	configuration := Configuration{}
	err := decoder.Decode(&configuration)
	if err != nil {
		fmt.Println("error:", err)
	}
	return (configuration)
}

func getTasks(conf Configuration) []string {
	taskTree := fmt.Sprintf("https://api.github.com/repos/%s/%s/git/trees/main", conf.Name, conf.Reponame)
	resp, err := http.Get(taskTree)
	if err != nil {
		log.Fatalln(err)
	}
	//Here im parse json
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatalln(err)
	}
	sb := string(body)
	//var result struct gitTree {}
	/*and here plase for some magik!
	im not undestand how it completly works, but it works!
	Like classic says: "It's alive!"
	*/
	var result map[string][]interface{}
	var resq []string
	json.Unmarshal([]byte(sb), &result)
	for _, v := range result["tree"] {
		entry := v.(map[string]interface{})
		if entry["type"] == "tree" {
			resq = append(resq, fmt.Sprintf("%v", entry["path"]))
		}
	}
	return resq
	/*After that somebody, please replace my hands back from
	the place, where the legs grows, back into the shoulders
	*/
}

func main() {
	conf := getargs()
	bot, err := tgbotapi.NewBotAPI(conf.Token)
	if err != nil {
		log.Panic(err)
	}

	bot.Debug = false

	log.Printf("Authorized on account %s", bot.Self.UserName)

	u := tgbotapi.NewUpdate(0)
	u.Timeout = 60

	updates, err := bot.GetUpdatesChan(u)

	for update := range updates {
		if update.Message == nil { // ignore any non-Message Updates
			continue
		}

		if update.Message.IsCommand() {
			command := update.Message.Command()
			switch command {
			case "git":
				repoUrl := fmt.Sprintf("https://github.com/%s/%s", conf.Name, conf.Reponame)
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, repoUrl)
				bot.Send(msg)
			case "tasks":
				var rString string = ""
				tasks := getTasks(conf)
				for i, t := range tasks {
					task := fmt.Sprintf("%d - %s ", i+1, t)
					rString = rString + task + "\n"
				}
				msg := tgbotapi.NewMessage(update.Message.Chat.ID, rString)
				bot.Send(msg)
			case "task":
				taskArgs := update.Message.CommandArguments()
				tasks := getTasks(conf)
				inputNum, err := strconv.Atoi(taskArgs)
				if err != nil {
					// handle error
					msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Got error task number: "+taskArgs)
					bot.Send(msg)
				}
				if inputNum > 0 {
					taskUrl := fmt.Sprintf("https://github.com/%s/%s/tree/main/%s", conf.Name, conf.Reponame, tasks[inputNum-1])
					msg := tgbotapi.NewMessage(update.Message.Chat.ID, taskUrl)
					bot.Send(msg)
				} else {
					msg := tgbotapi.NewMessage(update.Message.Chat.ID, "Got error task number: "+taskArgs)
					bot.Send(msg)
				}
			}
		}
	}
}
