from yt_dlp import YoutubeDL
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, TIT2, TALB, TPE1

# Specify playlist or individual song link
playlist_or_song = input(f'(P) - Playlist link\n(S) - Song link\n >> ')

link = input("Enter link: \n >> ")

yt_info = YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
info = yt_info.extract_info(link, download=False)

# Place song url(s) into string array
if playlist_or_song.lower() == "p":
    video_urls = [video['webpage_url'] for video in info['entries']]
elif playlist_or_song.lower() == "s":
    video_urls = [link]
else:
    print("Invalid input.")
    exit()

# Iterate through array, verify name of file & download
for entry in video_urls:
    video_info = yt_info.extract_info(entry, download=False)
    print(f"\nCURRENT TITLE: {video_info['title']}")
    new_title = input(f"NEW TITLE (optional, leave blank if no change is needed): \n >> ")

    if new_title == "":
        new_title = video_info['title']
        print("Title was not changed.\n")
    else:
        print("Title was changed.\n")

    filename = f"/Users/luca/Desktop/Media/Music/NewMusic_04-2023/{new_title}"

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        'outtmpl': f"{filename}.%(ext)s"
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry])

    print(f"\nSUCCESSFUL DOWNLOAD: {new_title}\n")

    # Read the ID3 tag or create one if not present
    try:
        tags = ID3(f"{filename}.mp3")
    except ID3NoHeaderError:
        print("Adding ID3 header")
        tags = ID3(filename=f"{filename}.mp3")
        tags.delete()  # delete existing ID3 tag if present
        tags.save(v2_version=3)  # set ID3 tag version to 2.3

    # Set title
    tags["TIT2"] = TIT2(encoding=3, text=new_title)

    # Set album name
    album = str(input("ALBUM: \n >> "))
    tags["TALB"] = TALB(encoding=3, text=album)

    # Set artist name
    artist = str(input("ARTIST: \n >> "))
    tags["TPE1"] = TPE1(encoding=3, text=artist)

    tags.save(f"{filename}.mp3")
    print("META DATA SAVED.")
