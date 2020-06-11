from pathlib import Path
import click, yaml, jinja2

@click.group()
def main():
    pass

def get_node_info(current_directory):
    with (current_directory / 'info.yaml').open() as f:
        return yaml.load(f)

latex_env = jinja2.Environment(
    loader = jinja2.PackageLoader(__name__, 'templates-latex'),
    autoescape = False,
    variable_start_string = '\VAR{',
    variable_end_string = '}')

def handle(current_directory):
    info = get_node_info(current_directory)
    template = latex_env.get_template(info['type'] + '.tex')
    print(template.render(info = info))

@main.command()
def build():
    print(get_node_info(Path('.')))
    handle(Path('.'))

