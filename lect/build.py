from pathlib import Path
from os import path
import jinja2, tempfile, subprocess, shutil
from lect.util import get_node_info

latex_env = jinja2.Environment(
    loader = jinja2.PackageLoader(__name__, 'templates-latex'),
    autoescape = False,
    trim_blocks = True,
    lstrip_blocks = True,
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    line_statement_prefix='%%',
    block_start_string = '\BLOCK{',
    block_end_string = '}')

def read_file(fi):
    with fi.open() as f:
        s = f.read()
    return s

def handle(current_directory):
    info = get_node_info(current_directory)
    print(info)

    if 'children' in info:
        info['rendered_children'] = map(lambda subdir: handle(current_directory / subdir), info['children'])
    try:
        template = latex_env.get_template(info['type'] + '.tex')
    except jinja2.exceptions.TemplateNotFound:
        if info['section']:
            template = latex_env.get_template('default-section.tex')
        else:
            template = latex_env.get_template('default.tex')

    return template.render(info = info, readf = lambda s: read_file(current_directory / s), hasf = lambda s: (current_directory / s).exists())

def build(output, tex):
    code = handle(Path('.'))

    if tex:
        if output == 'lecture.pdf':
            output = 'lecture.tex'
        with open(output, 'w') as f:
            f.write(code)
        return

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.tex') as tmp:
        tmp.write(code)
        tmpn = tmp.name

    with tempfile.TemporaryDirectory() as tmpd:
        print(tmpd)
        subprocess.run(['latexmk', '-pdf', tmpn, '-outdir=' + tmpd])
        p = Path(tmpn)
        shutil.copy(tmpd + '/' + p.stem + '.pdf', output)

    Path(tmpn).unlink()
