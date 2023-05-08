from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, TCOM, TCON, TDRC, TRCK

fname = "/Users/luca/Desktop/Media/Music/NewMusic_04-2023/song1test2.mp3"
# Read the ID3 tag or create one if not present
try:
    tags = ID3(fname)
except ID3NoHeaderError:
    print("Adding ID3 header")
    tags = ID3(filename=fname)
    tags.delete()  # delete existing ID3 tag if present
    tags.save(v2_version=3)  # set ID3 tag version to 2.3

tags["TIT2"] = TIT2(encoding=3, text=u"Daydreamin'")
tags["TALB"] = TALB(encoding=3, text=u'Yours Truly')
tags["TPE1"] = TPE1(encoding=3, text=u'Ariana Grande')
tags["TCON"] = TCON(encoding=3, text=u'R&B/Soul, Pop')
tags["TDRC"] = TDRC(encoding=3, text=u'2013')

tags.save(fname)
