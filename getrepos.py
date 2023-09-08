import sys
import requests

if len(sys.argv) != 2:
    print("Wrong argument number. Type \"help\" for help.")
    quit()

if sys.argv[1] == ('help' or '-help' or '--help'):
    print('Use: \ngetrepos.py <Github username>')
    quit()

repos_json = requests.get(f'https://api.github.com/users/{sys.argv[1]}/repos').json()

print(f"╔══╡{sys.argv[1]}\n║")
for repo in repos_json[:-1]:
    try:
        print(f"╠╦═╡{repo['html_url']}\n"
              f"║╚═╡{repo['description']}\n"
              f"║")
    except Exception as e:
        print(repos_json['message'])
        quit()

print(f"╚╦═╡{repos_json[-1]['html_url']}\n"
      f" ╚═╡{repos_json[-1]['description']}")