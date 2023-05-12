## This script extracts all of the zoning districts in relevant geojson files and outputs as a CSV.
# Thanks ChatGPT!
# Precursor to a script that looks up applicable districts for a parcel/lot.

import json
import os
import re
import pandas as pd

# List all geojson files in the directory that start with a number and underscore
files = [f for f in os.listdir('./source-gis/minneapolis') if f.endswith('.geojson') and re.match(r'^\d+_', f)]  # directory to be parametrized

# Initialize an empty list to store our data
data = []

for file in files:
    # Extract the priority number from the filename
    priority = int(file.split('_')[0])

    with open(file, 'r') as f:
        geojson = json.load(f)

        # Iterate over features in the geojson file
        for feature in geojson['features']:
            # Extract district
            district = feature['properties'].get('district', '')

            # Append to our data list
            data.append({
                'priority': priority,
                'file': file,
                'district': district
            })

# Convert the list to a pandas DataFrame
df = pd.DataFrame(data)

# Sort DataFrame by priority in descending order and district in ascending order
df = df.sort_values(by=['priority', 'district'], ascending=[False, True])

# Output DataFrame as a CSV file
df.to_csv('output.csv', index=False)
