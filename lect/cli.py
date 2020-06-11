from pathlib import Path
import click, yaml, jinja2

@click.group()
def main():
    pass

def get_node_info(current_directory):
    with (current_directory / 'info.yaml').open() as f:
        return yaml.safe_load(f)

latex_env = jinja2.Environment(
    loader = jinja2.PackageLoader(__name__, 'templates-latex'),
    autoescape = False,
    trim_blocks = True,
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    line_statement_prefix='%%',
    block_start_string = '\BLOCK{',
    block_end_string = '}')

def handle(current_directory):
    info = get_node_info(current_directory)

    if 'children' in info:
        info['rendered_children'] = map(lambda subdir: handle(current_directory / subdir), info['children'])

    template = latex_env.get_template(info['type'] + '.tex')
    return template.render(info = info)

@main.command()
def build():
    print(get_node_info(Path('.')))
    print(handle(Path('.')))

