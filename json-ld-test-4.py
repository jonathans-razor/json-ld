'''
A Python program that calls jsonplaceholder api and returns the response in JSON  format. This program to able to run from the command line like this:

python json-ld-test-4.py posts/1
python json-ld-test-4.py posts/2
python json-ld-test-4.py posts/3

'''

import requests
import sys
import json

def fetch_data(endpoint):
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fetch_data.py <endpoint>")
        sys.exit(1)
    
    endpoint = sys.argv[1]
    data = fetch_data(endpoint)
    print(json.dumps(data, indent=4))
