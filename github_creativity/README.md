#

## Description

This script check open pull requests for a repository.

## Requirements

- Python3
- Python3 modules: colored

## Prepare usage

To avoid github api limitation you can use personal token for requests.
Learn more  about [rate limit](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) and [how to make personal token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

## Usage

Run script and pass url to it:

```sh
./check_pull.py https://github.com/$user/$repo
```

Also, you can use your token :

```sh
./check_pull.py -u {USERNAME} -t {TOKEN} https://github.com/$user/$repo
```
