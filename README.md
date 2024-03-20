## jspf-to-xspf
This is a fork of https://github.com/mckar/jspf-to-xspf

The main change from the fork is making this work with JSPFs exported from ListenBrainz.
You can then use the resulting file to import the XSPF playlist to soundiiz.com.

Requires python library [xspf](https://github.com/alastair/xspf) from alastair - I just put `xspf.py` next to `jspf_to_xspf.py`.

## Usage
jspf_to_xspf.py -i "import-JSPF-file" -e "export-XSPF-file" <br>
jspf_to_xspf.py -i playlist.json -e playlist.xspf <br>