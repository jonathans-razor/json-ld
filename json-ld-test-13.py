import requests
import json

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        print(json.dumps(posts, indent=4))
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_users()
