from mindee import Client, documents

# Init a new client
mindee_client = Client(api_key="Your API key")

# Load a file from disk
image_path = "./path to your receipt image (jpg or png)"
input_doc = mindee_client.doc_from_path(image_path)

# Parse the document by passing the appropriate type
api_response = input_doc.parse(documents.TypeReceiptV4)

# Print a brief summary of the parsed data
print(api_response.document)