import click, lect.build, lect.add

@click.group()
def main():
    pass

@main.command(help='Create a LaTeX document for the lecture.')
@click.option('--output', default='lecture.pdf', help='Set the name of the output file.')
@click.option('--tex/--pdf', default=False, help='Produce LaTeX code instead of a PDF.')
def build(output, tex):
    lect.build.build(output, tex)

@main.command(help='Add a new section or entry.')
@click.argument('type')
@click.argument('name')
@click.option('--section', '-S', 'category', flag_value='section', help='Create a section.')
@click.option('--autodetect', 'category', flag_value='autodetect', default=True, help='Try to infer from the type whether to create a section or entry (this is the default).')
@click.option('--entry', '-E', 'category', flag_value='entry', help='Create an entry.')
@click.option('--number', '-n', default=-1, help="The number of the entry. Do not specify to let LaTeX figure it out on its own.")
@click.option('--numbered/--unnumbered', ' /-u', 'numbered', default=True, help='Enables or disables numbering of entries')
def add(type, name, category, numbered, number):
    lect.add.add(name, type, category, numbered, number)
