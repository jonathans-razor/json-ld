import json
from pyld import jsonld

# Sample JSON-LD document
doc = {
    "@context": {
        "name": "http://schema.org/name",
        "homepage": {
            "@id": "http://schema.org/url",
            "@type": "@id"
        },
        "image": {
            "@id": "http://schema.org/image",
            "@type": "@id"
        }
    },
    "name": "Manu Sporny",
    "homepage": "http://manu.sporny.org/",
    "image": "http://manu.sporny.org/images/manu.png"
}

# Compact the document
compacted = jsonld.compact(doc, doc['@context'])
print("Compacted JSON-LD:")
print(json.dumps(compacted, indent=2))

# Expand the document
expanded = jsonld.expand(doc)
print("\nExpanded JSON-LD:")
print(json.dumps(expanded, indent=2))
