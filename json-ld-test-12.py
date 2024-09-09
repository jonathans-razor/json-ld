import requests
import json

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    
    if response.status_code == 200:
        users = response.json()
        json_ld = {
            "@context": "https://schema.org",
            "@type": "Person",
            "users": users
        }
        print(json.dumps(json_ld, indent=4))
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_users()
