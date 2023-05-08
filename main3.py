# importing packages
from pytube import YouTube
import os

# url input from user
yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
destination = "/Users/luca/Desktop/Media/Music/NewMusic_04-2023/"

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = f"{base} - .mp3"
os.rename(out_file, new_file)

# result of success
print(yt.title + " has been successfully downloaded.")
# print(yt.metadata['Song'])
# print(yt.metadata['Artist'])
# print(yt.metadata['Album'])
