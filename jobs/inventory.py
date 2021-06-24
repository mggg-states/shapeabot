#!/usr/bin/env /home/max/.pyenv/shims/python

import os
import subprocess
import geopandas as gpd
import glob
import json


os.chdir(os.environ["dir"])

with open("../../inventory.json") as f:
    items = list(json.load(f))

shapefiles = glob.glob("*.zip")
for shapefile in shapefiles:
    shp = gpd.read_file(shapefile)

    items.append(
        {
            "name": os.environ["name"],
            "state": os.environ["state"],
            "shapefile": shapefile.split("/")[-1],
            "columns": list(shp.columns),
        }
    )

with open("../../inventory.json", "w") as f:
    json.dump(list(items), f)