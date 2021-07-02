#!/usr/bin/env python3
import requests
import argparse
from termcolor import colored


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
    print ('Found [{}] opened pull requests'.format(colored(str(len(open_pulls)), 'green')))
    productive_contributors = []
    uniq_contributors = []
    for pull_req in open_pulls:
        if pull_req['user']['login'] in uniq_contributors:
            productive_contributors.append(pull_req['user']['login'])
        else:
            uniq_contributors.append(pull_req['user']['login'])

    print('Most productive contributors are:')
    for username in set(productive_contributors):
        print('{}: {}'.format(colored(username, 'cyan'), colored(str(productive_contributors.count(username)+1), 'magenta')))

else:
    print('Got {} status of response'.format(r_pulls.status_code))
