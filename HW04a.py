import requests
import json

def GitHub(id):
    #sets url with the users id
    url = "https://api.github.com/users/" + str(id) + "/repos"
    #gets the url
    account = requests.get(url)
    status = account.status_code

    if status == 404:
        print("This is not an account")
    #gets the json
    account = account.json()
    #for all repos in the users acct

    repolist = []
    for repo in account:
        #sets url with repos
        commitsurl = "https://api.github.com/repos/" + str(id) + "/" + str(repo["name"]) + "/commits"
        #gets the url
        commits = requests.get(commitsurl) 
        #sets counter
        num = 0
        #for the commits in the json count how many there are
        for commit in commits.json():
            num = num + 1
        #print the repo with its name and number of commits
        repolist.append("Repo: " + str(repo["name"]) + " Number of commits: " + str(num))
        #print("Repo: " + str(repo["name"]) + " Number of commits: " + str(num))
    return repolist
