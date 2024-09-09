import requests
import json
from pyld import jsonld

def fetch_and_frame_jsonld():
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
        
        # Step 5: Define a frame
        frame = {
            "@context": context["@context"],
            "@type": "http://schema.org/Person",
            "address": {
                "@type": "http://schema.org/PostalAddress",
                "street": "http://schema.org/streetAddress",
                "city": "http://schema.org/addressLocality",
                "zipcode": "http://schema.org/postalCode",
                "geo": {
                    "@type": "http://schema.org/GeoCoordinates",
                    "lat": "http://schema.org/latitude",
                    "lng": "http://schema.org/longitude"
                }
            },
            "company": {
                "@type": "http://schema.org/Organization",
                "companyName": "http://schema.org/name",
                "catchPhrase": "http://schema.org/description",
                "bs": "http://schema.org/keywords"
            }
        }
        
        # Step 6: Frame the JSON-LD data
        framed_jsonld = jsonld.frame(json_data_with_context, frame)
        
        # Step 7: Print the framed JSON-LD data
        print(json.dumps(framed_jsonld, indent=2))
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_and_frame_jsonld()