# xboomx

xboomx is wrapper around the dmenu. It is also a launcher. All the things it done is just sorting commands to launch according to their launch frequency. In other words - if you launch emacs and lxterminal all the time - they will appear in the list of commands first.

## Installation
```sh
git clone https://github.com/victorhaggqvist/xboomx
cd xboomx
sudo apt-get install suckless-tools # here is instrtuction for debian. really we need only dmenu
sudo python setup.py install
mkdir ~/.xboomx
cp etc/config ~/.xboomx/config
```

Available via AUR as `xboomx-snilius`.

### Migration to xboomx 0.7.x, python 3
xboomx 0.7.x contain breaking changes from previous versions.

To perform the migration make sure you still have python 2 installed, then run `xboomx_python2mirgation.py` which performs the migration. When this is done you are good to start using xboomx 0.7.x.

## Config
The config file, which if you followed the instructions above is located at `~/.xboomx/config`, contains the following a json object.
```json
{
  "dmenu_params": "-b -i -nb black -nf orange -sb black -p \"#\"",
  "ignorelist": ["X"],
  "complete_offpath": false
}
```

For `dmenu_params` please see the manpages for dmenu.
```sh
man dmenu
```

The `ignorelist` to prevent stuff that is in your path for showing up as suggestions. Like if you type `x` then `X` might show up before `xbmc`.

`complete_offpath` will add everything that's in you ranking database regardless of availability on PATH. This is off by default. 

## License

    xboomx
    Copyright (C) 2014-2015  Victor Häggqvist

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

For original license see the file `LICENSE.org`

This is a fork of https://bitbucket.org/dehun/xboomx
