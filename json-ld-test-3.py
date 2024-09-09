import requests
import json
from pyld import jsonld
import sys

def fetch_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def convert_to_jsonld(data):
    context = {
        "@context": {
            "userId": "http://schema.org/identifier",
            "id": "http://schema.org/identifier",
            "title": "http://schema.org/name",
            "body": "http://schema.org/text"
        }
    }
    jsonld_data = jsonld.compact(data, context)
    return jsonld_data

def main(api_url):
    data = fetch_api_data(api_url)
    jsonld_data = convert_to_jsonld(data)
    print(json.dumps(jsonld_data, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <API_URL>")
        sys.exit(1)
    
    api_url = sys.argv[1]
    main(api_url)
