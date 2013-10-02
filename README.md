gfmviewer-wx : Github Flavour Markdown viewer for wxPython
==========================================================

The gfmviewer script converts a Github Flavoured Markdown file in to HTML
and displays it using wxPython. The conversion is done using the Github
API and so requires an active Internet connection. Changes to the source
file will automatically update the HTML display.

By default a proper file notification library will be used to watch the
file. However if this is not available - or it is explicitly disabled with
the --poll option - the file's modification time will be checked once a
second. Any change to said time will be considered a modification and
trigger an HTML update.

![gfmviewer screenshot](https://raw.github.com/vrai/gfmviewer-wx/master/screenshot.png)

Usage
-----

Usage information can be displayed using the -h or --help arguments. These
are:

    gfmviewer [-h] [-f] [-p] [FILE]

    positional arguments:
      FILE        markdown file to display

    optional arguments:
      -h, --help  show this help message and exit
      -f, --fork  fork a copy of the process in to the background and then
                  return immediately (leaving the background process running)
      -p, --poll  always poll for file changes, even if file notification is
                  available


Install
-------

Installation instructions can be found in the INSTALL file.


Updates and license
-------------------

The latest version of this script can be downloaded from Github:

    https://github.com/vrai/gfmviewer-wx

The gfmviewer is free software and is licensed under version 2 of the GNU
General Public License as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along
with this program (see the LICENSE file); if not, write to the Free
Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA.

---

Copyright 2013
Vrai Stacey <vrai.stacey@gmail.com>
