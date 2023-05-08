import yt_dlp

ydl = yt_dlp.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

video_url = str(input('Enter URL: \n >> '))
info = ydl.extract_info(video_url, download=False)

title = info['title']
uploader = info['uploader']
description = info['description']

print(f'\nTitle: {title}')
print(f'Uploader: {uploader}')
print(f'Description: {description}')
