from flask import Flask, render_template, request
from jinja2 import Environment, FileSystemLoader
import requests, json, os, datetime

app = Flask(__name__)
app.debug = True

# Define the template directory
tpldir = os.path.dirname(os.path.abspath(__file__))

# Setup the template enviroment
env = Environment(loader=FileSystemLoader(tpldir), trim_blocks=True)

# Page size
PAGE_SIZE = 100

url = "https://api.github.com/search/repositories"

@app.route('/')
def search():
    # search_term = "arrow"
    search_term = request.args.get('search_term')
    print(search_term)
    querystring = {"q":search_term}
    response = requests.request("GET", url, params=querystring)

    items = json.loads(response.text)["items"][:PAGE_SIZE]
    items = sorted(items, key=lambda k: k['created_at'], reverse=True)

    my_data = []
    # loop for top five items and get commit details
    for item in items[:4]:
        my_item = {}
        print(item["name"])
        my_item["repository_name"] = item["name"]
        # basic string hack, remove T and Z
        my_item["created_at"] = item["created_at"][:-1].replace("T", " ")
        # incoming date format2016-08-24T20:56:45Z
        # created = datetime.datetime.strptime(item["created_at"],
        # "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
        my_item["owner_url"] = item["owner"]["url"]
        my_item["avatar_url"] = item["owner"]["avatar_url"]
        my_item["owner_login"] = item["owner"]["login"]
        # print(item["commits_url"][:-6])

        commits = json.loads(requests.request("GET", item["commits_url"][:-6]).text)
        # print(commits)
        if(len(commits) > 0):
            commit = commits[0]
            my_item["sha"] = commit["sha"]
            my_item["commit_message"] = commit["commit"]["message"]
            my_item["commit_author_name"] = commit["commit"]["author"]["name"]

        my_data.append(my_item)

    d = {"respository_name": "Abcd", "created_at": "123",
        "owner_url": "google.com", "avatar_url":"abc.com",
        "owner_login":"hello", "sha":"adf", "commit_message":"random", "commit_author_name":"me"}
    # loopdata.append(d)
    return env.get_template("template.html").render(search_term = search_term, my_data = my_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





