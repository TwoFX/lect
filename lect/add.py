from pathlib import Path
from lect.util import get_node_info
import yaml

def add(name, type, category):
    info = get_node_info(Path('.'))

    if not 'children' in info:
        info['children']  = []
    info['children'].append(name)

    with open('info.yaml', 'w') as f:
        f.write(yaml.dump(info, default_flow_style = False, sort_keys = False))

    Path(name).mkdir()

    newinfo = {}
    newinfo['type'] = type
    newinfo['label'] = name

    if category == 'section':
        newinfo['section'] = True
    elif category == 'entry':
        newinfo['section'] = False
    else:
        newinfo['section'] = type in ['chapter', 'section', 'subsection', 'subsubsection', 'subsubsubsection', 'paragraph']

    with (Path(name) / 'info.yaml').open('w') as f:
        f.write(yaml.dump(newinfo, default_flow_style = False, sort_keys = False))

    print(f"Created a new {type} called {name}.")
