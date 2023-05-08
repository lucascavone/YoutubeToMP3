import yt_dlp

# Set the playlist URL
playlist_url = str(input('Enter link:\n >> '))

# Create a yt_dlp instance
ydl = yt_dlp.YoutubeDL()

# Extract the playlist information
playlist_info = ydl.extract_info(playlist_url, download=False)

# Extract the titles of the videos in the playlist
video_titles = [video['title'] for video in playlist_info['entries']]
video_urls = [video['webpage_url'] for video in playlist_info['entries']]

# Print the list of video titles
print(video_titles)
print(video_urls)
