'''
A Python program that calls the Jsonplaceholder API and returns the response in JSON-LD format. This 
program is able to run from the command line like this:

python json-ld-test-6.py
'''
import requests
import json

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        json_ld_data = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "posts": []
        }
        for item in data:
            post = {
                "@type": "BlogPosting",
                "headline": item["title"],
                "articleBody": item["body"],
                "author": {
                    "@type": "Person",
                    "name": f"User {item['userId']}"
                },
                "identifier": item["id"]
            }
            json_ld_data["posts"].append(post)
        return json_ld_data
    else:
        return {"error": "Failed to fetch data"}

if __name__ == "__main__":
    data = fetch_data()
    print(json.dumps(data, indent=4))
