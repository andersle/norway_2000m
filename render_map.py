# -*- coding: utf-8 -*-
# Copyright (c) 2018, Anders Lervik.
# Distributed under the LGPLv2.1+ License. See LICENSE for more info.
"""Generate a map of the 2000 m peaks in Norway."""
from operator import itemgetter
import json
import jinja2


def main():
    """Load the mountains and ender the map using the template."""
    mountains = []
    with open('2000m.json', 'r') as infile:
        mountains = json.load(infile)
    mountains_sorted = sorted(mountains, key=itemgetter('name'))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    data = {'mountains': mountains_sorted}
    render = env.get_template('template.html').render(data)
    with open('2000m.html', 'w') as output:
        output.write(render)


if __name__ == '__main__':
    main()
