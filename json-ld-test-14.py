import requests
import json

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        json_ld = {
            "@context": "https://schema.org",
            "@type": "Post",
            "posts": posts
        }
        print(json.dumps(json_ld, indent=4))
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_users()
