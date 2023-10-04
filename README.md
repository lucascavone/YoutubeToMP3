# YouTube-to-MP3 Converter With Metadata Editor
**Warning**: Converting YouTube videos to MP3 files may be a 
violation of YouTube's terms of service and may infringe on 
copyright laws. Please use this tool responsibly and for personal, 
non-commercial use only. The libraries used in this project are 
open-source and freely available, but please do not use this tool 
for any commercial or profit-making purposes.
## Usage
This program will accept either a specific YouTube song or playlist 
link. Before downloading a song, it will ask the user to change the
filename if needed, and will prompt the user for the artist and album
name which are added as metadata to the file. 
## Installation
Use the code provided in the `main.py` file. Import the **yt_dlp** python library using `pip install yt-dlp` and 
the **Mutagen** python library using the `pip install mutagen`. 
 
## Development
I chose personalization over automation when developing this
project since I wanted to be able to manually control the filename, 
album name and artist.   

I used the [yt_dlp](https://github.com/yt-dlp/yt-dlp) python library
to set the audio specifications and convert the YouTube videos to MP3
files. I used the [Mutagen](https://mutagen.readthedocs.io/en/latest/)
library to access and modify the audio file metadata. I chose to
only modify the artist and album name, however the Mutagen library can
be used to modify all ID3 metadata tags if needed. Similarly, the
yt_dlp library has a built-in function to download YouTube playlists.
Since I wanted to be able to modify the filename for each song if
needed, I decided to iterate through each song in the playlist without
using the built-in function.

## Troubleshooting
It may be necessary to download and install the **ffmpeg** and **ffprobe** software from this [link](https://ffmpeg.org/download.html).

[Update - 03/10/2023] At the time of developing this program, I recall using the **ffmpeg** and **ffprobe** packages. However, recent testing has indicated the contrary. This README has been updated accordingly.
