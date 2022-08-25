from algoliasearch.search_client import SearchClient
import csv
# Connect and authenticate with your Algolia app and Admin Key
client = SearchClient.create("####", "####")


# Create a new index and add a record
index = client.init_index("demo_products")

res = index.browse_objects(
    {'query': "apple", 'attributesToRetrieve': ['name', 'brand']})

csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
                                "objectID", "name", "brand"])
        writer.writeheader()
        for data in res:
            writer.writerow(data)
except IOError:
    print("I/O error")
