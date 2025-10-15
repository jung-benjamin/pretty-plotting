#! /usr/bin/env python3

import importlib.resources as pkg_resources
import json

from cycler import cycler

with pkg_resources.open_text('prettyplotting', 'rwth_colors.json') as f:
    rwth_colors = {
        n: [i / 255 for i in col]
        for n, col in json.load(f).items()
    }

rwth_cycler_75 = cycler(color=[
    rwth_colors[n] for n in [
        "blau-75",
        "orange-75",
        "grun-75",
        "magenta-75",
        "yellow-75",
        "petrol-75",
        "turkis-75",
        "maigrun-75",
        "rot-75",
        "violett-75",
        "bordeaux-75",
        "lila-75",
    ]
])

rwth_cycler = cycler(color=[
    rwth_colors[n] for n in [
        "blau",
        "orange",
        "grun",
        "magenta",
        "yellow",
        "petrol",
        "turkis",
        "maigrun",
        "rot",
        "violett",
        "bordeaux",
        "lila",
    ]
])

if __name__ == '__main__':
    for n, col in rwth_colors.items():
        print(f'{n}: {col}')
