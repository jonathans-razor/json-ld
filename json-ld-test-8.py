'''
Even though this code seems to work, the flattened version doesn't have the graph keyword.
'''
import requests
import json
from pyld import jsonld

# Function to fetch data from JSONPlaceholder API
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    return response.json()

# Function to convert data to JSON-LD format
def convert_to_jsonld(data):
    context = {
        "@context": {
            "userId": "http://schema.org/identifier",
            "id": "http://schema.org/identifier",
            "title": "http://schema.org/name",
            "body": "http://schema.org/text"
        }
    }
    data_with_context = {**data, **context}
    compacted = jsonld.compact(data_with_context, context["@context"])
    expanded = jsonld.expand(data_with_context)
    flattened = jsonld.flatten(data_with_context)
    return compacted, expanded, flattened

# Main function
def main():
    data = fetch_data()
    compacted, expanded, flattened = convert_to_jsonld(data)
    
    print("\n")
    print("Compacted JSON-LD:")
    print(json.dumps(compacted, indent=2))
    
    print("\n")
    print("\nExpanded JSON-LD:")
    print(json.dumps(expanded, indent=2))

    print("\n")
    print("\nFlattened JSON-LD:")
    print(json.dumps(flattened, indent=2))

if __name__ == "__main__":
    main()
