#! /usr/bin/env python3

import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, 'rwth_colors.json'), 'r') as f:
    color_data = json.load(f)

rwth_colors = {n: [i / 255 for i in col] for n, col in color_data.items()}

if __name__ == '__main__':
    for n, col in rwth_colors.items():
        print(f'{n}: {col}')
