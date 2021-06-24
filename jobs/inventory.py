#!/usr/bin/env /home/max/.pyenv/shims/python

import os
import subprocess
import geopandas as gpd
import glob
import json
import maup
import shapely


os.chdir(os.environ["dir"])

if os.path.isfile("../../output/inventory.json"):
    with open("../../output/inventory.json") as f:
        items = list(json.load(f))
else:
    items = []

shapefiles = glob.glob("*.zip")
for shapefile in shapefiles:
    shp = gpd.read_file(shapefile)

    try:
        overlaps = maup.repair.count_overlaps(shp)
        gaps = len(maup.repair.holes_of_union(shp))
        topological_errors = 0
    except shapely.errors.TopologicalError:
        overlaps = 0
        gaps = 0 
        topological_errors = 1

    items.append(
        {
            "name": os.environ["name"],
            "state": os.environ["state"],
            "shapefile": shapefile.split("/")[-1],
            "columns": list(shp.columns),
            "overlaps": overlaps,
            "gaps": gaps,
            "topological_errors": topological_errors
        }
    )

with open("../../output/inventory.json", "w") as f:
    json.dump(list(items), f)
