#!powershell -ExecutionPolicy Bypass -Command

import sys
import requests

if len(sys.argv) != 2:
    print("Wrong argument number. Type \"help\" for help.")
    quit()

if sys.argv[1] == ('help' or '-help' or '--help'):
    print('Use: getrepos.py <Github username>')
    quit()

repos = requests.get(f'https://api.github.com/users/{sys.argv[1]}/repos')
repos_json = repos.json()

for repo in repos_json:
    try:
        print (f"{repo['html_url']} \n {repo['description']} \n")
    except Exception as e:
        print(repos_json['message'])
        quit()