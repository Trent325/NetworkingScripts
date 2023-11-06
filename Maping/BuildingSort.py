import json

# Load the JSON data from the file
with open('BuildingCoordinates.json', 'r') as file:
    data = json.load(file)

# Initialize a list for the formatted objects
formatted_data = []

# Iterate through the 'response' array in the JSON data
for item in data.get('response', []):
    additional_info = item.get('additionalInfo', [])
    for info in additional_info:
        if 'nameSpace' in info and info['nameSpace'] == 'Location':
            attributes = info.get('attributes', {})

            name = item.get('name')
            latitude_str = attributes.get('latitude')
            longitude_str = attributes.get('longitude')

            if name and latitude_str and longitude_str:
                latitude = float(latitude_str)
                longitude = float(longitude_str)

                # Create a formatted object
                formatted_object = {
                    "Name": name,
                    "Location": {
                        "type": "Point",
                        "coordinates": [longitude, latitude]
                    }
                }

                formatted_data.append(formatted_object)

# Save the formatted data to a file
with open('output_formatted.json', 'w') as output_file:
    json.dump(formatted_data, output_file, indent=2)
