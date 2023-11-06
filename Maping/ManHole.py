import pandas as pd
import re

# Read data from Excel sheet
excel_file = 'Coordinate.xlsx'
df = pd.read_excel(excel_file)

# Create a list to store the objects
objects = []

# Define a regular expression pattern to match coordinates
coordinate_pattern = r'(\d+)°(\d+)\'([\d.]+)\"([NS]) (\d+)°(\d+)\'([\d.]+)\"([EW])'

for index, row in df.iterrows():
    enclosure_number = row['Encosure #']
    coordinates = row['Coordinates']

    # Use regular expression to extract components
    match = re.match(coordinate_pattern, coordinates)

    if match:
        lat_deg, lat_min, lat_sec, lat_dir, lon_deg, lon_min, lon_sec, lon_dir = match.groups()

        # Calculate latitude and longitude in decimal degrees
        latitude = float(lat_deg) + float(lat_min) / 60 + float(lat_sec) / 3600
        if lat_dir == 'S':
            latitude = -latitude  # Southern hemisphere is negative latitude

        longitude = float(lon_deg) + float(lon_min) / 60 + float(lon_sec) / 3600
        if lon_dir == 'W':
            longitude = -longitude  # Western hemisphere is negative longitude

        # Create the object
        enclosure_object = {
            
            "Name": f"Enclosure {enclosure_number}",
            "Location": {
                "type": "Point",
                "coordinates": [longitude, latitude]
            }
        }

        # Append the object to the list
        objects.append(enclosure_object)
    else:
        print(f"Invalid coordinate format for row {index + 2}: {coordinates}")

# Print the created objects (you can also save them to MongoDB)
for obj in objects:
    print(obj)
import pandas as pd
import re
import json

# Read data from Excel sheet
excel_file = 'Coordinate.xlsx'
df = pd.read_excel(excel_file)

# Create a list to store the objects
objects = []

# Define a regular expression pattern to match coordinates
coordinate_pattern = r'(\d+)°(\d+)\'([\d.]+)\"([NS]) (\d+)°(\d+)\'([\d.]+)\"([EW])'

for index, row in df.iterrows():
    enclosure_number = row['Encosure #']
    coordinates = row['Coordinates']

    # Use regular expression to extract components
    match = re.match(coordinate_pattern, coordinates)

    if match:
        lat_deg, lat_min, lat_sec, lat_dir, lon_deg, lon_min, lon_sec, lon_dir = match.groups()

        # Calculate latitude and longitude in decimal degrees
        latitude = float(lat_deg) + float(lat_min) / 60 + float(lat_sec) / 3600
        if lat_dir == 'S':
            latitude = -latitude  # Southern hemisphere is negative latitude

        longitude = float(lon_deg) + float(lon_min) / 60 + float(lon_sec) / 3600
        if lon_dir == 'W':
            longitude = -longitude  # Western hemisphere is negative longitude

        # Create the object
        enclosure_object = {
            "Name": f"Enclosure {enclosure_number}",
            "Location": {
                "type": "Point",
                "coordinates": [longitude, latitude]
            }
        }

        # Append the object to the list
        objects.append(enclosure_object)
    else:
        print(f"Invalid coordinate format for row {index + 2}: {coordinates}")

# Save the objects to a JSON file
with open('enclosure_objects.json', 'w') as json_file:
    json.dump(objects, json_file)

# Print the created objects (you can also save them to MongoDB)
for obj in objects:
    print(obj)
