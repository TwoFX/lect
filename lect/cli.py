import click, lect.build, lect.add

@click.group()
def main():
    pass

@main.command(help='Create a LaTeX document for the lecture')
@click.option('--output', default='lecture.pdf', help='Set the name of the output file.')
@click.option('--tex/--pdf', default=False, help='Produce LaTeX code instead of a PDF.')
def build(output, tex):
    lect.build.build(output, tex)

@main.command(help='Add a new section or entry')
@click.argument('type')
@click.argument('name')
def add(type, name):
    lect.add.add(name, type)
