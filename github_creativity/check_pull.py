#!/usr/bin/env python3
import requests
import argparse
import colored


parser = argparse.ArgumentParser(description='This script check open pull requests for a repository.\n\
    Input link to github repository and enjoy')
parser.add_argument("url", help = "Url of target Github repository", type = str, action = "store")
parser.add_argument("-u", "--user", help = "Username to login at GitHub", type = str, action = "store")
parser.add_argument("-t", "--token", help = "Your personal GitHub token", type = str, action = "store")
args = parser.parse_args()

if args.token != None or args.user !=None :
    work_with_auth = True
else:
    work_with_auth = False

try:
    repo={'user':args.url.split('/')[3], 'repo':args.url.split('/')[4]}
except Exception as err:
    print('Can not parse url string. Please, try another.')

if work_with_auth:
    r_pulls = requests.get('http://api.github.com/repos/{}/{}/pulls?per_page=100'.format(repo['user'], repo['repo']), auth=(args.user, args.token))
else:
    r_pulls = requests.get('http://api.github.com/repos/{}/{}/pulls?per_page=100'.format(repo['user'], repo['repo']))

if r_pulls.status_code == 200:
    open_pulls = r_pulls.json()
    print ('Found [{}] opened pull requests'.format(
        colored.fg('green')+ str(len(open_pulls)) + colored.style.RESET))
    productive_contributors = []
    uniq_contributors = []
    contributor_labels = {}
    for pull_req in open_pulls:
        if pull_req['user']['login'] in uniq_contributors:
            productive_contributors.append(pull_req['user']['login'])
        else:
            contributor_labels.update({pull_req['user']['login']:[]})
            uniq_contributors.append(pull_req['user']['login'])
        if len (pull_req['labels']) > 0 :
            for label in pull_req['labels']:
                newlabel = colored.fg('#' + label['color']) + label['name'] + colored.style.RESET
                contributor_labels[pull_req['user']['login']].append(newlabel)


    print('Most productive contributors are:')
    for username in set(productive_contributors):
        print('{}: {}. Labels: {}'.format(
            colored.fg('green') + colored.attr('bold') + username +colored.style.RESET, 
            colored.fg('magenta') + str(productive_contributors.count(username)+1) +colored.style.RESET,
            ' '.join(set(contributor_labels[username]))
        ))

else:
    print('Got {} status of response'.format(r_pulls.status_code))
