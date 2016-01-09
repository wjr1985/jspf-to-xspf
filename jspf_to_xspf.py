import xspf
import json
import argparse

parser = argparse.ArgumentParser(description = 'Convert JSPF file to XSPF')
parser.add_argument('-i', dest = "importfile", required = True, help = "Import JSPF filename")
parser.add_argument('-e', dest = "exportfile", required = True, help = "Export XSPF filename")
args = parser.parse_args()

x = xspf.Xspf()
fj = open(args.importfile,'r')
jdata = json.load(fj)
for playlist in jdata["playlists"]:
  print("Converting Playlist %s" % playlist["title"])
  x.title = "%s" % playlist["title"]
# You can set these attributes:
# title, creator, annotation, info, location, identifier, image, date, license
  for track in playlist["tracks"]:
    # Add tracks by creating a Track object
    tr1 = xspf.Track()
    tr1.title = "%s" % track["title"]
    tr1.creator = "%s" % track["artist"]
    tr1.album = "%s" % track["album"]
    x.add_track(tr1)
fj.close()

# write XSPF content to file
fx = open(args.exportfile,'wb')
fx.write(x.toXml())
fx.close()