import requests
import json
from pyld import jsonld

def fetch_and_flatten_jsonld():
    # Step 1: Make a GET request to the JSONPlaceHolder Users API
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    # Step 2: Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the JSON response
        json_data = response.json()
        
        # Step 4: Add a context to the JSON data
        context = {
            "@context": {
                "name": "http://schema.org/name",
                "username": "http://schema.org/alternateName",
                "email": "http://schema.org/email",
                "address": "http://schema.org/address",
                "street": "http://schema.org/streetAddress",
                "suite": "http://schema.org/suite",
                "city": "http://schema.org/addressLocality",
                "zipcode": "http://schema.org/postalCode",
                "geo": "http://schema.org/geo",
                "lat": "http://schema.org/latitude",
                "lng": "http://schema.org/longitude",
                "phone": "http://schema.org/telephone",
                "website": "http://schema.org/url",
                "company": "http://schema.org/organization",
                "companyName": "http://schema.org/name",
                "catchPhrase": "http://schema.org/description",
                "bs": "http://schema.org/keywords"
            }
        }
        
        # Combine context with the JSON data and wrap in @graph
        json_data_with_context = {
            "@context": context["@context"],
            "@graph": json_data
        }
        
        # Step 5: Flatten the JSON-LD data
        flattened_jsonld = jsonld.flatten(json_data_with_context)
        
        # Step 6: Print the flattened JSON-LD data
        print(json.dumps(flattened_jsonld, indent=2))
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_and_flatten_jsonld()