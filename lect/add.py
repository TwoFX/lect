from pathlib import Path
from lect.util import get_node_info
import click, yaml

def add(name, type, category, numbered, number):
    info = get_node_info(Path('.'))

    if 'section' in info and not info['section']:
        click.confirm('Trying to create a child of a non-section. Do you want to continue?', abort=True)

    if not 'children' in info:
        info['children']  = []
    info['children'].append(name)

    with open('info.yaml', 'w') as f:
        f.write(yaml.dump(info, default_flow_style = False, sort_keys = False))

    Path(name).mkdir()

    newinfo = {}
    newinfo['type'] = type
    newinfo['label'] = name
    newinfo['numbered'] = numbered

    if number != -1:
        newinfo['number'] = number

    if category == 'section':
        newinfo['section'] = True
    elif category == 'entry':
        newinfo['section'] = False
    else:
        newinfo['section'] = type in ['chapter', 'section', 'subsection', 'subsubsection', 'subsubsubsection', 'paragraph']

    if newinfo['section']:
        newinfo['title'] = click.prompt('Title', type=str, default=name)

    with (Path(name) / 'info.yaml').open('w') as f:
        f.write(yaml.dump(newinfo, default_flow_style = False, sort_keys = False))

    if not newinfo['section']:
        Path(Path(name) / 'statement.tex').touch()

    print(f"Created a new {type} called {name}.")
