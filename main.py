import json
import re

def sort_json(obj):
    # If the object is a dictionary, sort its keys
    if isinstance(obj, dict):
        return {k: sort_json(obj[k]) for k in sorted(obj)}
    # If the object is a list, sort its elements using the 'Name' key
    elif isinstance(obj, list) and all(isinstance(e, dict) for e in obj):
        return [sort_json(e) for e in sorted(obj, key=lambda x: x.get('Name', ''))]
    else:
        return obj

# Regular expression to remove the keys
key_regex = r'(NUUID|ISODate|NumberLong|\(|\)|)|Date'

# Load the first JSON object
with open('local.json', 'r') as f:
    json_string = f.read()
    # Remove the keys from the JSON string
    cleaned_json_string = re.sub(key_regex, '', json_string)
    # Load the JSON object
    data1 = json.loads(cleaned_json_string)

# Load the second JSON object
with open('dev.json', 'r') as f:
    json_string = f.read()
    # Remove the keys from the JSON string
    cleaned_json_string = re.sub(key_regex, '', json_string)
    # Load the JSON object
    data2 = json.loads(cleaned_json_string)

# Sort the keys of each JSON object and its nested objects and arrays
sorted_data1 = sort_json(data1)
sorted_data2 = sort_json(data2)

# Write the sorted JSON objects to the files
with open('local.json', 'w') as f:
    json.dump(sorted_data1, f, indent=2)

with open('dev.json', 'w') as f:
    json.dump(sorted_data2, f, indent=2)
