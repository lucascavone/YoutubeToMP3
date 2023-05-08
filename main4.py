from pytube import YouTube

link = str(input("Enter link: \n >> "))
yt = YouTube(link)

print("Searching for audio track...")

# Try using get_audio_only() instead of filter(only_audio=True).first()
downloader = yt.streams.get_audio_only()
if downloader is None:
    print("Could not find audio track")
    exit()

print(f"Downloading... {yt.title} by {yt.author}")
downloader.download()
print("File downloaded.")
