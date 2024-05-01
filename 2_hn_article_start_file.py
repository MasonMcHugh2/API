import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json','w')

json.dump(r.json(),outfile,indent=4)

submission_list = r.json()


url = 'https://hacker-news.firebaseio.com/v0/item/39994391.json'
r = requests.get(url)
outfile = open('hn2.json','w')
json.dump(r.json(),outfile,indent=4)

article_dict = r.json()

print(f"Title: {article_dict['title']}")
if 'descendants' in article_dict:
    print(f"Comments: {article_dict['descendants']}")
print(f"URL: {article_dict['url']}")

for i in submission_list[0:20]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
    r = requests.get(url)
   
    article_dict = r.json()

    print(f"Title: {article_dict['title']}")
    if 'descendants' in article_dict:
        print(f"Comments: {article_dict['descendants']}")
    print(f"URL: {article_dict['url']}")

    print()
    print()
