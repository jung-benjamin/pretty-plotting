#! /usr/bin/env python3

import re
import os

definecolor_regex = re.compile(r"""(
                                    (\{.+\})
                                    \s*
                                    \{RGB\}
                                    (\{\s*\d{1,3}\s+\d{1,3}\s+\d{1,3}\})
                                    )""",
                                    re.VERBOSE)

rwth_colors = {}

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, 'rwth_colors'), 'r') as f:
    text = f.read()
    for groups in definecolor_regex.findall(text):
        name = groups[1].strip('{}')
        # lstrip is necessary to remove leading whitespace,
        # otherwise re.split adds an empty string (as per documentation)
        rgb_str = re.split(r'\s+', groups[2].strip('{}').lstrip())
        rgb_val = [float(i)/255 for i in rgb_str]
        rwth_colors[name] = rgb_val

if __name__ == '__main__':
    for n, col in rwth_colors.items():
        print(f'{n}: {col}')
