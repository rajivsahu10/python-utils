import click

@click.command()
def less():
    click.echo_via_pager('\n'.join('Line %d' % idx
                                   for idx in range(200)))