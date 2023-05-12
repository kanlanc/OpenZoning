# The function find_intersecting_districts takes a list of coordinates and a file folder as arguments, and returns a list of tuples (priority, filename without prefix or suffix, district).
# Call this function with the coordinates of the parcel and the folder where your .geojson files are stored.
# The script will output the tuples for each district that intersects with the parcel, sorted by the priority number.
# Thanks ChatGPT!

import re
import os
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon

def find_intersecting_districts(parcel_coords, file_folder):
    # Create a Shapely polygon from the coordinates
    parcel = gpd.GeoSeries(Polygon(parcel_coords))

    # List all geojson files in the directory that start with a number and underscore
    files = [f for f in os.listdir(file_folder) if f.endswith('.geojson') and re.match(r'^\d+_', f)]

    # Initialize an empty list to store our data
    data = []

    # Sort files based on priority
    files = sorted(files, key=lambda x: int(x.split('_')[0]))

    for file in files:
        # Extract the priority number from the filename
        priority = int(file.split('_')[0])
        file_name = re.sub(r'(\d+_)(.*)(\.geojson)', r'\2', file)

        # Load the geojson file into a geopandas GeoDataFrame
        gdf = gpd.read_file(os.path.join(file_folder, file))

        # Check for intersection with the parcel
        intersection = gdf[gdf.geometry.intersects(parcel.iloc[0])]

        # For each intersecting district, append priority, file name, and district to our data list
        for index, row in intersection.iterrows():
            data.append((priority, file_name, row['district']))

    return data

# Assume parcel is given as a list of coordinates
parcel_coords = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]  # replace with actual coordinates
file_folder = './path_to_your_files'  # replace with your folder path

data = find_intersecting_districts(parcel_coords, file_folder)

# Print the resulting list of tuples
for item in data:
    print(item)
