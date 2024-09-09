import requests
import json

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        users = response.json()
        print(json.dumps(users, indent=4))
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_users()
