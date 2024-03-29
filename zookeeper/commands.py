import click
from panoptes_client.panoptes import PanoptesAPIException

from .zootils import utils


@click.command()
@click.argument('imgdir')
@click.argument('projid')
@click.option(
    '-s', '--subject',
    default=False,
    nargs=1,
    help='Designate subject set id'
)
@click.option(
    '-q', '--quiet',
    default=False,
    is_flag=True,
    help='Silences output when uploading images to zooniverse'
)
@click.pass_context
def upload(ctx, imgdir, projid, subject, quiet):
    ''' Uploads images from the image directory to zooniverse project '''
    from .zootils import upload

    try:
        utils.connect(un=ctx.obj['un'], pw=ctx.obj['pw'])
    except PanoptesAPIException as e:
        exit(e)
    upload(imgdir, projid, subject, quiet)

    return


@click.command()
@click.argument('projid')
@click.argument('outfile')
@click.option(
    '-t', '--exp_type',
    default='classifications',
    help='Specify the type of export. Check Zooniverse help for available types'
)
@click.option(
    '-g', '--no_generate',
    default=False,
    is_flag=True,
    help='Download an existing one rather than generating one'
)
@click.pass_context
def export(ctx, projid, outfile, exp_type, no_generate):
    ''' Gets export from zooniverse project '''
    from .zootils import export
    try:
        utils.connect(un=ctx.obj['un'], pw=ctx.obj['pw'])
    except PanoptesAPIException as e:
        exit(e)
    export(projid, outfile, exp_type, no_generate)

    return


@click.command()
@click.argument('imgdir')
def manifest(imgdir):
    ''' Generate a manifest in the directory specified by imgdir '''
    from .zootils import manifest

    manifest(imgdir)

    return
