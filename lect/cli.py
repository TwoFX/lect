import click, lect.build

@click.group()
def main():
    pass

@main.command()
@click.option('--output', default='lecture.pdf', help='Set the name of the output file.')
@click.option('--tex/--pdf', default=False, help='Produce LaTeX code instead of a PDF.')
def build(output, tex):
    lect.build.build(output, tex)

