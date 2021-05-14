"""nodepy.cli: provides entry point main()."""


__version__ = "0.0.1"


import os
import sys
import json
import click

from nodepy.errors import *

@click.group()
@click.pass_context
def main(ctx):
    click.secho(f'nodepy version {__version__}', bold=True)
    ctx.ensure_object(dict)

    ctx.obj['PROJECT_INFO'] = None
    if 'project.json' in os.listdir():
        with open('project.json', 'r') as f:
            project_info = json.load(f)
        
        ctx.obj['PROJECT_INFO'] = project_info

@main.command()
@click.option('--name', prompt='Name of project', help='Name of project')
@click.option(
    '--mainscript',
    prompt='Main Script',
    help='The main script',
    default='main.py'
)
@click.pass_context
def init(ctx, name, mainscript):
    """Initializes a project."""
    if ctx.obj.get('PROJECT_INFO'):
        raise ProjectFound('Found Project')

    with open('project.json', 'w') as f:
        json.dump({
            'name': name,
            'main': mainscript,
            'scripts': {
                'main': f'python {mainscript}'
            }
        }, f, indent=4)

    click.echo('Wrote \'project.json\'')

    if mainscript not in os.listdir():
        with open(mainscript, 'w') as f:
            f.write('# Write your Python Code here!')

        click.echo(f'Wrote \'{mainscript}\'')

@main.command()
@click.argument('script_name')
@click.pass_context
def run(ctx, script_name):
    """Runs a script within the project."""
    project_info = ctx.obj.get('PROJECT_INFO')
    if not project_info:
        raise ProjectNotFound('Could not find project')

    scripts = project_info['scripts']
    script = scripts.get(script_name)
    if script:
        click.secho(f'> {script}')
        os.system(script)
    else:
        raise ScriptNotFound('Script not found')
