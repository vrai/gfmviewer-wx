from distutils.core import setup

setup (
    name = 'gfmviewer',
    version = '0.1.0',
    description = 'View a Github Formatted Markdown file as formatted HTML',
    scripts = [ 'gfmviewer' ],
    author = 'Vrai Stacey',
    author_email = 'vrai.stacey@gmail.com',
    url = 'http://github.com/vrai/gfmviewer-wx',
    license = 'GPL',
    long_description = """\
Converts a Github Flavoured Markdown file in to HTML - using the Github API -
and displays it. The source file is monitored and will be reformatted /
displayed on any change.

By default a proper file notification library will be used to watch the file.
However if this is not available, or it is disabled with the --poll option,
the file's modification time will be checked once a second.

On most platforms (current not including OS X) the --fork option will cause
the viewer to run in the background, detached from the terminal used to start
it. """ )

# vim: ft=python:sw=4:ts=4:et
