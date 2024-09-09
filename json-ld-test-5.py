'''
A Python program that calls jsonplaceholder api and returns the response in JSON format. This 
program is able to run from the command line. 
'''
import requests
import json

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

if __name__ == "__main__":
    data = fetch_data()
    print(json.dumps(data, indent=4))
