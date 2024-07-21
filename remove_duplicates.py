############
# this is a useful script you can run if you end up with duplicates in your saved problems.json file
############
import json

# Function to remove duplicates from lists in the JSON data
def remove_duplicates_from_json(file_path):
    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Remove duplicates from each list
    # Iterate through each key in the dictionary. If the value associated with a key is a list, convert it to a set to remove duplicates, then convert it back to a list.
    for key in data:
        if isinstance(data[key], list):
            data[key] = list(set(data[key]))
    print("duplicates removed!")
    # Write the updated JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Replace with the path to your JSON file
remove_duplicates_from_json('problems.json')
