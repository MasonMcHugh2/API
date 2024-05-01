import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open('output.json','w')

response_dict = r.json()

json.dump(response_dict,outfile,indent=4)

#print out how many repos are in this file

list_of_repos = response_dict['items']

print(len(list_of_repos))

first_repo = list_of_repos[0]

#print out the number of keys in first_repo

print(f"Number of keys: {len(first_repo)}")


for key in first_repo:
    print(key)

#Exercise
#print out the full name, the url, the license name and topics
#for the first repo

print(f"Full Name: {first_repo['full_name']}")
print(f"URL: {first_repo['owner']['html_url']}")
print(f"License Name: {first_repo['license']['name']}")
print(f"Topics: {first_repo['topics']}")
for i in first_repo['topics']:
    print(f"Topic: {i}")

repo_names, stars = [], []

for repo in list_of_repos[:10]:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

from plotly.graph_objs import bar
from plotly import offline

data = [
    {
        'type': 'bar',
        'x': repo_names,
        'y':stars,
        'marker':{
            'color':'rgb(60,100,150)',
            'line':{"width":1.5,'color':'rgb(25,25,25)'},
        },
        'opacity':0.6,
    }
]

my_layout = {
    'title':'Most Starred Python Projects on GitHub',
    'xaxis':{"title":"repository"},
    'yaxis':{'title':'Stars'}
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig,filename='python_repos.html')
