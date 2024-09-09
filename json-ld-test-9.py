import requests
from pyld import jsonld
import json

# Function to fetch data from Jsonplaceholder API
def fetch_data():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()

# Function to convert data to JSON-LD format
def convert_to_jsonld(data):
    context = {
        "@context": {
            "userId": "http://schema.org/identifier",
            "id": "http://schema.org/identifier",
            "title": "http://schema.org/name",
            "completed": "http://schema.org/Boolean"
        }
    }
    jsonld_data = {
        "@graph": [data],
        "@context": context["@context"]
    }
    return jsonld_data

# Main function
def main():
    data = fetch_data()
    jsonld_data = convert_to_jsonld(data)

    # Compacted format
    compacted = jsonld.compact(jsonld_data, jsonld_data['@context'])
    print("\nCompacted JSON-LD:")
    print(json.dumps(compacted, indent=2))

    # Expanded format
    expanded = jsonld.expand(jsonld_data)
    print("\nExpanded JSON-LD:")
    print(json.dumps(expanded, indent=2))

    # Flattened format
    flattened = jsonld.flatten(jsonld_data)
    print("\nFlattened JSON-LD:")
    print(json.dumps(flattened, indent=2))

if __name__ == "__main__":
    main()
