#! /usr/bin/env python3

import importlib.resources as pkg_resources
import json

with pkg_resources.open_text('prettyplotting', 'rwth_colors.json') as f:
    rwth_colors = {n: [i / 255 for i in col] for n, col in json.load(f).items()}

if __name__ == '__main__':
    for n, col in rwth_colors.items():
        print(f'{n}: {col}')
